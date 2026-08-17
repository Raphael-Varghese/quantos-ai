from pathlib import Path
import random


INPUT_FILE = Path("data/raw/merged.txt")

TRAIN_FILE = Path("data/raw/train.txt")
VAL_FILE = Path("data/raw/val.txt")

SEED = 1337
VAL_FRACTION = 0.10


def main():

    print("=" * 70)
    print("SPLITTING MERGED MOSAIC DATASET")
    print("=" * 70)
    print()

    text = INPUT_FILE.read_text(encoding="utf-8")

    examples = [
        x.strip()
        for x in text.split("<bos>")
        if x.strip()
    ]

    print(f"Total examples: {len(examples):,}")

    random.seed(SEED)
    random.shuffle(examples)

    val_count = max(
        1,
        round(len(examples) * VAL_FRACTION)
    )

    val_examples = examples[:val_count]
    train_examples = examples[val_count:]

    train_text = "\n\n".join(
        "<bos>\n" + example
        for example in train_examples
    ) + "\n"

    val_text = "\n\n".join(
        "<bos>\n" + example
        for example in val_examples
    ) + "\n"

    TRAIN_FILE.write_text(
        train_text,
        encoding="utf-8"
    )

    VAL_FILE.write_text(
        val_text,
        encoding="utf-8"
    )

    print()
    print(f"Training examples:   {len(train_examples):,}")
    print(f"Validation examples: {len(val_examples):,}")
    print()

    print(f"Training characters:   {len(train_text):,}")
    print(f"Validation characters: {len(val_text):,}")
    print()

    print(f"Saved: {TRAIN_FILE}")
    print(f"Saved: {VAL_FILE}")
    print()
    print("Split complete.")


if __name__ == "__main__":
    main()
