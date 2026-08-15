from pathlib import Path

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import ByteLevel
from tokenizers.trainers import BpeTrainer


# ============================================================
# Paths
# ============================================================

TRAIN_FILE = Path(
    "data/raw/train.txt"
)

OUTPUT_DIR = Path(
    "data/processed/tokenizer"
)

OUTPUT_FILE = (
    OUTPUT_DIR / "tokenizer.json"
)


# ============================================================
# Configuration
# ============================================================

VOCAB_SIZE = 8000

MIN_FREQUENCY = 2


# ============================================================
# Validate dataset
# ============================================================

if not TRAIN_FILE.exists():

    raise FileNotFoundError(
        f"Training file not found: {TRAIN_FILE}"
    )


# ============================================================
# Create tokenizer
# ============================================================

tokenizer = Tokenizer(
    BPE(
        unk_token="<unk>"
    )
)


tokenizer.pre_tokenizer = ByteLevel(
    add_prefix_space=False
)


# ============================================================
# Trainer
# ============================================================

trainer = BpeTrainer(
    vocab_size=VOCAB_SIZE,

    min_frequency=MIN_FREQUENCY,

    special_tokens=[
        "<pad>",
        "<unk>",
        "<bos>",
        "<eos>",
        "<system>",
        "<user>",
        "<assistant>",
        "<end>",
    ]
)


# ============================================================
# Train
# ============================================================

print(
    "Training BPE tokenizer..."
)

tokenizer.train(
    files=[
        str(TRAIN_FILE)
    ],
    trainer=trainer
)


# ============================================================
# Save
# ============================================================

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

tokenizer.save(
    str(OUTPUT_FILE)
)


# ============================================================
# Report
# ============================================================

print()

print(
    f"Tokenizer saved to: "
    f"{OUTPUT_FILE}"
)

print(
    f"Vocabulary size: "
    f"{tokenizer.get_vocab_size():,}"
)


# ============================================================
# Test
# ============================================================

test_text = (
    "Write a Python function that adds "
    "two numbers."
)

encoded = tokenizer.encode(
    test_text
)

print()

print(
    "Test text:"
)

print(
    test_text
)

print()

print(
    "Tokens:"
)

print(
    encoded.tokens
)

print()

print(
    "Token IDs:"
)

print(
    encoded.ids
)

print()

print(
    f"Token count: "
    f"{len(encoded.ids)}"
)