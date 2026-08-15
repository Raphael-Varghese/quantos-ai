import math
import os
import time
import random

import torch

from .config import (
    DEVICE,
    SEED,
    MAX_STEPS,
    EVAL_INTERVAL,
    EVAL_STEPS,
    LEARNING_RATE,
    MIN_LEARNING_RATE,
    WARMUP_STEPS,
    WEIGHT_DECAY,
    GRADIENT_ACCUMULATION_STEPS,
    GRADIENT_CLIP,
    CHECKPOINT_DIR,
    CHECKPOINT_FILE,
    RESUME_FROM_CHECKPOINT,
)

from .dataset import TextDataset
from .model import GPT


# ============================================================
# Reproducibility
# ============================================================

random.seed(SEED)
torch.manual_seed(SEED)


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
# Checkpoint loading
# ============================================================

start_step = 0


if (
    RESUME_FROM_CHECKPOINT
    and os.path.exists(CHECKPOINT_FILE)
):

    print(
        f"Loading checkpoint: "
        f"{CHECKPOINT_FILE}"
    )

    checkpoint = torch.load(
        CHECKPOINT_FILE,
        map_location=DEVICE,
        weights_only=False
    )

    checkpoint_vocab_size = checkpoint[
        "vocab_size"
    ]

    if checkpoint_vocab_size != vocab_size:

        raise ValueError(
            "Checkpoint vocabulary does not "
            "match the current dataset vocabulary."
        )

    model.load_state_dict(
        checkpoint["model"]
    )

    optimizer.load_state_dict(
        checkpoint["optimizer"]
    )

    start_step = (
        checkpoint["step"] + 1
    )

    print(
        f"Resuming from step "
        f"{start_step}"
    )

    print()


# ============================================================
# Learning-rate schedule
# ============================================================

def get_learning_rate(step):

    if step < WARMUP_STEPS:

        return (
            LEARNING_RATE
            * (step + 1)
            / WARMUP_STEPS
        )

    if MAX_STEPS <= WARMUP_STEPS:

        return MIN_LEARNING_RATE

    progress = (
        (step - WARMUP_STEPS)
        /
        (MAX_STEPS - WARMUP_STEPS)
    )

    progress = min(
        max(progress, 0.0),
        1.0
    )

    cosine = (
        0.5
        *
        (
            1.0
            +
            math.cos(
                math.pi * progress
            )
        )
    )

    return (
        MIN_LEARNING_RATE
        +
        (
            LEARNING_RATE
            - MIN_LEARNING_RATE
        )
        * cosine
    )


# ============================================================
# Evaluation
# ============================================================

@torch.no_grad()
def evaluate():

    model.eval()

    results = {}

    for split in (
        "train",
        "validation"
    ):

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
            sum(losses)
            /
            len(losses)
        )

    model.train()

    return results


# ============================================================
# Checkpoint saving
# ============================================================

def save_checkpoint(step):

    os.makedirs(
        CHECKPOINT_DIR,
        exist_ok=True
    )

    torch.save(
        {
            "model":
                model.state_dict(),

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

            "config": {
                "block_size":
                    dataset.data.shape[0]
                    if False
                    else None
            },

            "seed":
                SEED,

            "parameter_count":
                parameter_count,
        },
        CHECKPOINT_FILE
    )

    print(
        f"Checkpoint saved: "
        f"{CHECKPOINT_FILE}"
    )


# ============================================================
# Training
# ============================================================

print("Starting training...")

start_time = time.time()


for step in range(
    start_step,
    MAX_STEPS
):

    # --------------------------------------------------------
    # Learning rate
    # --------------------------------------------------------

    learning_rate = (
        get_learning_rate(step)
    )

    for parameter_group in (
        optimizer.param_groups
    ):

        parameter_group[
            "lr"
        ] = learning_rate

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
            f"lr {learning_rate:.6e} | "
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
            loss
            /
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
    # Optimizer update
    # --------------------------------------------------------

    optimizer.step()

    # --------------------------------------------------------
    # Checkpoint
    # --------------------------------------------------------

    if (
        step > start_step
        and step % EVAL_INTERVAL == 0
    ):

        save_checkpoint(step)


# ============================================================
# Final checkpoint
# ============================================================

save_checkpoint(
    MAX_STEPS - 1
)

print()

print(
    "Training complete."
)

print(
    f"Model saved to {CHECKPOINT_FILE}"
)