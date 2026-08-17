from pathlib import Path

from tokenizers import Tokenizer
from tokenizers.decoders import ByteLevel
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import ByteLevel as ByteLevelPreTokenizer
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
MIN_FREQUENCY = 1


# ============================================================
# Validation
# ============================================================

if not TRAIN_FILE.exists():

    raise FileNotFoundError(
        f"Training file not found: {TRAIN_FILE}"
    )


# ============================================================
# Tokenizer
# ============================================================

tokenizer = Tokenizer(
    BPE(
        unk_token="<unk>",
        byte_fallback=True
    )
)

tokenizer.pre_tokenizer = (
    ByteLevelPreTokenizer(
        add_prefix_space=False
    )
)

tokenizer.decoder = ByteLevel()


# ============================================================
# Trainer
# ============================================================

trainer = BpeTrainer(
    vocab_size=VOCAB_SIZE,
    min_frequency=MIN_FREQUENCY,

    initial_alphabet=(
        ByteLevelPreTokenizer.alphabet()
    ),

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

print("Training BPE tokenizer...")
print(
    f"Dataset: {TRAIN_FILE}"
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
    f"Tokenizer saved: {OUTPUT_FILE}"
)

print(
    f"Vocabulary size: "
    f"{tokenizer.get_vocab_size():,}"
)


# ============================================================
# Test
# ============================================================

test_text = (
    "<bos>\n"
    "<system>\n"
    "You are Mosaic.\n\n"
    "<user>\n"
    "Write a Python function that adds two numbers.\n\n"
    "<assistant>\n"
    "def add(a, b):\n"
    "    return a + b\n\n"
    "<end>"
)

encoded = tokenizer.encode(
    test_text
)

decoded = tokenizer.decode(
    encoded.ids,
    skip_special_tokens=False
)

print()

print(
    "Round-trip test:"
)

print()

print(
    "Expected:"
)

print(
    repr(test_text)
)

print()

print(
    "Decoded:"
)

print(
    repr(decoded)
)

print()

if decoded == test_text:

    print(
        "Round-trip test: PASS"
    )

else:

    print(
        "Round-trip test: FAIL"
    )

    raise RuntimeError(
        "Tokenizer round-trip test failed."
    )