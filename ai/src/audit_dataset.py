from pathlib import Path
from collections import Counter
import re


RAW_DIR = Path("data/raw")
TRAIN_FILE = RAW_DIR / "train.txt"


def normalize(text):
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_examples(text):
    """
    Extract <bos> ... <end> records.
    """
    pattern = re.compile(
        r"<bos>\s*(.*?)\s*<end>",
        re.DOTALL
    )

    return [
        normalize(match)
        for match in pattern.findall(text)
    ]


def main():

    print("=" * 70)
    print("MOSAIC DATASET AUDIT")
    print("=" * 70)
    print()

    files = sorted(
        path
        for path in RAW_DIR.glob("*.txt")
        if path.name != "train.txt"
    )

    all_examples = []
    file_counts = {}

    for path in files:

        text = path.read_text(
            encoding="utf-8"
        )

        examples = extract_examples(text)

        file_counts[path.name] = len(examples)

        all_examples.extend(examples)

        print(
            f"{path.name:25} "
            f"examples={len(examples):4d} "
            f"chars={len(text):7,d}"
        )

    print()
    print("-" * 70)

    counts = Counter(all_examples)

    duplicates = {
        example: count
        for example, count in counts.items()
        if count > 1
    }

    print(
        f"Total source examples: "
        f"{len(all_examples):,}"
    )

    print(
        f"Unique examples:       "
        f"{len(counts):,}"
    )

    print(
        f"Duplicate examples:    "
        f"{len(duplicates):,}"
    )

    print(
        f"Duplicate records:     "
        f"{sum(duplicates.values()) - len(duplicates):,}"
    )

    print()

    if duplicates:

        print("DUPLICATES")
        print("=" * 70)

        for index, (example, count) in enumerate(
            sorted(
                duplicates.items(),
                key=lambda item: item[1],
                reverse=True
            ),
            start=1
        ):

            print()
            print(
                f"[{index}] repeated {count} times"
            )

            print(
                example[:500]
            )

            if index >= 20:
                break

    print()
    print("=" * 70)

    if TRAIN_FILE.exists():

        train_text = TRAIN_FILE.read_text(
            encoding="utf-8"
        )

        train_examples = extract_examples(
            train_text
        )

        print(
            f"Current train.txt examples: "
            f"{len(train_examples):,}"
        )

        print(
            f"Current train.txt chars:    "
            f"{len(train_text):,}"
        )

    print()
    print("Audit complete.")


if __name__ == "__main__":
    main()