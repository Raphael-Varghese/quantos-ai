import torch

from .config import (
    DEVICE,
    BATCH_SIZE,
    BLOCK_SIZE,
    CHECKPOINT_FILE,
    EVAL_STEPS,
)

from .dataset import TextDataset
from .model import GPT


# ============================================================
# Load dataset
# ============================================================

dataset = TextDataset()


# ============================================================
# Load checkpoint
# ============================================================

print()
print("Loading checkpoint...")

checkpoint = torch.load(
    CHECKPOINT_FILE,
    map_location=DEVICE,
    weights_only=False
)

vocab_size = checkpoint[
    "vocab_size"
]


# ============================================================
# Model
# ============================================================

model = GPT(
    vocab_size
).to(DEVICE)

model.load_state_dict(
    checkpoint["model"]
)

model.eval()


# ============================================================
# Evaluation
# ============================================================

@torch.no_grad()
def evaluate_split(split):

    losses = []

    for _ in range(
        EVAL_STEPS
    ):

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

    return (
        sum(losses)
        /
        len(losses)
    )


# ============================================================
# Run
# ============================================================

print()
print("=" * 60)
print("MOSAIC EVALUATION")
print("=" * 60)

print(
    f"Checkpoint step: "
    f"{checkpoint.get('step', 'unknown')}"
)

print()

train_loss = evaluate_split(
    "train"
)

validation_loss = evaluate_split(
    "validation"
)

print(
    f"Training loss:   "
    f"{train_loss:.4f}"
)

print(
    f"Validation loss: "
    f"{validation_loss:.4f}"
)

print()