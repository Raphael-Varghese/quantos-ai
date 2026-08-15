from pathlib import Path

import numpy as np

from .subword_tokenizer import SubwordTokenizer


# ============================================================
# Paths
# ============================================================

INPUT_FILE = Path(
    "data/raw/train.txt"
)

OUTPUT_DIR = Path(
    "data/processed"
)

TRAIN_FILE = (
    OUTPUT_DIR / "train.bin"
)

VAL_FILE = (
    OUTPUT_DIR / "val.bin"
)


# ============================================================
# Configuration
# ============================================================

TRAIN_SPLIT = 0.85

# ============================================================
# Load text
# ============================================================

if not INPUT_FILE.exists():

    raise FileNotFoundError(
        f"Dataset not found: {INPUT_FILE}"
    )


print(
    f"Loading dataset: {INPUT_FILE}"
)

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as file:

    text = file.read()


print(
    f"Characters: {len(text):,}"
)


# ============================================================
# Tokenizer
# ============================================================

tokenizer = SubwordTokenizer()

print(
    f"Vocabulary: "
    f"{tokenizer.vocab_size:,}"
)


# ============================================================
# Encode
# ============================================================

print(
    "Tokenizing dataset..."
)

tokens = tokenizer.encode(
    text
)

tokens = np.asarray(
    tokens,
    dtype=np.uint16
)


print(
    f"Tokens: {len(tokens):,}"
)


# ============================================================
# Train / validation split
# ============================================================

split = int(
    len(tokens) * TRAIN_SPLIT
)

train_tokens = tokens[:split]

val_tokens = tokens[split:]


# ============================================================
# Save
# ============================================================

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


train_tokens.tofile(
    TRAIN_FILE
)

val_tokens.tofile(
    VAL_FILE
)


# ============================================================
# Report
# ============================================================

print()

print(
    f"Training tokens: "
    f"{len(train_tokens):,}"
)

print(
    f"Validation tokens: "
    f"{len(val_tokens):,}"
)

print()

print(
    f"Saved: {TRAIN_FILE}"
)

print(
    f"Saved: {VAL_FILE}"
)

print()

print(
    "Dataset processing complete."
)