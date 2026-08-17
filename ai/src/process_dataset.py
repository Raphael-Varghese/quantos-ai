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

TRAIN_SPLIT = 0.90

SEED = 1337


# ============================================================
# Load
# ============================================================

if not INPUT_FILE.exists():

    raise FileNotFoundError(
        f"Dataset not found: {INPUT_FILE}"
    )


text = INPUT_FILE.read_text(
    encoding="utf-8"
)


# ============================================================
# Split by complete examples
# ============================================================

examples = [
    block.strip()
    for block in text.split("<bos>")
    if block.strip()
]


if len(examples) < 10:

    raise ValueError(
        "Dataset contains too few examples."
    )


split = int(
    len(examples) * TRAIN_SPLIT
)


train_examples = examples[:split]
val_examples = examples[split:]


train_text = "\n\n".join(
    "<bos>\n" + example
    for example in train_examples
)

val_text = "\n\n".join(
    "<bos>\n" + example
    for example in val_examples
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

print("Tokenizing training data...")

train_tokens = np.asarray(
    tokenizer.encode(train_text),
    dtype=np.uint16
)

print("Tokenizing validation data...")

val_tokens = np.asarray(
    tokenizer.encode(val_text),
    dtype=np.uint16
)


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
print("=" * 60)
print("DATASET PROCESSING")
print("=" * 60)

print(
    f"Total examples:      {len(examples):,}"
)

print(
    f"Training examples:   {len(train_examples):,}"
)

print(
    f"Validation examples: {len(val_examples):,}"
)

print()

print(
    f"Training tokens:     {len(train_tokens):,}"
)

print(
    f"Validation tokens:   {len(val_tokens):,}"
)

print()

print(
    f"Saved: {TRAIN_FILE}"
)

print(
    f"Saved: {VAL_FILE}"
)