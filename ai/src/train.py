import os
import time

import torch

from .config import (
    DEVICE,
    MAX_STEPS,
    EVAL_INTERVAL,
    EVAL_STEPS,
    LEARNING_RATE,
    WEIGHT_DECAY,
    GRADIENT_ACCUMULATION_STEPS,
    GRADIENT_CLIP,
    CHECKPOINT_DIR,
    CHECKPOINT_FILE,
)

from .dataset import TextDataset

from .model import GPT


# ============================================================
# Dataset
# ============================================================

dataset = TextDataset()

vocab_size = dataset.tokenizer.vocab_size


# ============================================================
# Model
# ============================================================

model = GPT(
    vocab_size
).to(DEVICE)


parameter_count = sum(
    parameter.numel()
    for parameter in model.parameters()
)


print()
print(
    f"Model parameters: "
    f"{parameter_count:,}"
)

print(
    f"Device: {DEVICE}"
)

print()


# ============================================================
# Optimizer
# ============================================================

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=LEARNING_RATE,
    weight_decay=WEIGHT_DECAY
)


# ============================================================
# Evaluation
# ============================================================

@torch.no_grad()
def evaluate():

    model.eval()

    results = {}

    for split in [
        "train",
        "validation"
    ]:

        losses = []

        for _ in range(EVAL_STEPS):

            x, y = dataset.get_batch(
                split
            )

            _, loss = model(
                x,
                y
            )

            losses.append(
                loss.item()
            )

        results[split] = (
            sum(losses) / len(losses)
        )

    model.train()

    return results


# ============================================================
# Training
# ============================================================

print("Starting training...")

start_time = time.time()


for step in range(MAX_STEPS):

    # --------------------------------------------------------
    # Evaluation
    # --------------------------------------------------------

    if (
        step % EVAL_INTERVAL == 0
        or step == MAX_STEPS - 1
    ):

        losses = evaluate()

        elapsed = (
            time.time() - start_time
        )

        print(
            f"step {step:5d} | "
            f"train {losses['train']:.4f} | "
            f"val {losses['validation']:.4f} | "
            f"time {elapsed:.1f}s"
        )

    # --------------------------------------------------------
    # Gradient accumulation
    # --------------------------------------------------------

    optimizer.zero_grad(
        set_to_none=True
    )

    for _ in range(
        GRADIENT_ACCUMULATION_STEPS
    ):

        x, y = dataset.get_batch(
            "train"
        )

        _, loss = model(
            x,
            y
        )

        loss = (
            loss /
            GRADIENT_ACCUMULATION_STEPS
        )

        loss.backward()

    # --------------------------------------------------------
    # Gradient clipping
    # --------------------------------------------------------

    torch.nn.utils.clip_grad_norm_(
        model.parameters(),
        GRADIENT_CLIP
    )

    # --------------------------------------------------------
    # Update
    # --------------------------------------------------------

    optimizer.step()

    # --------------------------------------------------------
    # Checkpoint
    # --------------------------------------------------------

    if (
        step > 0
        and step % EVAL_INTERVAL == 0
    ):

        os.makedirs(
            CHECKPOINT_DIR,
            exist_ok=True
        )

        torch.save(
            {
                "model": model.state_dict(),

                "tokenizer_stoi":
                    dataset.tokenizer.stoi,

                "tokenizer_itos":
                    dataset.tokenizer.itos,

                "vocab_size":
                    vocab_size,

                "step":
                    step,

                "optimizer":
                    optimizer.state_dict(),
            },
            CHECKPOINT_FILE
        )

        print(
            f"Checkpoint saved: "
            f"{CHECKPOINT_FILE}"
        )


# ============================================================
# Final save
# ============================================================

os.makedirs(
    CHECKPOINT_DIR,
    exist_ok=True
)

torch.save(
    {
        "model": model.state_dict(),

        "tokenizer_stoi":
            dataset.tokenizer.stoi,

        "tokenizer_itos":
            dataset.tokenizer.itos,

        "vocab_size":
            vocab_size,

        "step":
            MAX_STEPS,

        "optimizer":
            optimizer.state_dict(),
    },
    CHECKPOINT_FILE
)

print()
print("Training complete.")
print(
    f"Model saved to {CHECKPOINT_FILE}"
)