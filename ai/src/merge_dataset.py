from pathlib import Path
from collections import OrderedDict


# ============================================================
# Configuration
# ============================================================

MOSAIC_FILE = Path(
    "data/raw/train.txt"
)

OASST_FILE = Path(
    "data/external/oasst1/oasst1_clean.txt"
)

OUTPUT_FILE = Path(
    "data/raw/merged.txt"
)


# ============================================================
# Parsing
# ============================================================

def parse_examples(text):

    examples = []

    for chunk in text.split("<bos>"):

        chunk = chunk.strip()

        if not chunk:
            continue

        if "<system>" not in chunk:
            continue

        if "<user>" not in chunk:
            continue

        if "<assistant>" not in chunk:
            continue

        if "<end>" not in chunk:
            continue

        system = (
            chunk
            .split("<system>", 1)[1]
            .split("<user>", 1)[0]
            .strip()
        )

        user = (
            chunk
            .split("<user>", 1)[1]
            .split("<assistant>", 1)[0]
            .strip()
        )

        assistant = (
            chunk
            .split("<assistant>", 1)[1]
            .split("<end>", 1)[0]
            .strip()
        )

        if not system or not user or not assistant:
            continue

        examples.append(
            {
                "system": system,
                "user": user,
                "assistant": assistant,
            }
        )

    return examples


# ============================================================
# Question normalization
# ============================================================

def normalize_question(text):

    return " ".join(
        text.lower().split()
    )


# ============================================================
# Formatting
# ============================================================

def format_example(example):

    return (
        "<bos>\n"
        "<system>\n"
        f"{example['system']}\n\n"
        "<user>\n"
        f"{example['user']}\n\n"
        "<assistant>\n"
        f"{example['assistant']}\n\n"
        "<end>"
    )


# ============================================================
# Main
# ============================================================

def main():

    print("=" * 70)
    print("MERGING MOSAIC + OPENASSISTANT")
    print("=" * 70)
    print()

    mosaic_text = MOSAIC_FILE.read_text(
        encoding="utf-8"
    )

    oasst_text = OASST_FILE.read_text(
        encoding="utf-8"
    )

    mosaic = parse_examples(
        mosaic_text
    )

    oasst = parse_examples(
        oasst_text
    )

    print(
        f"Mosaic examples:       {len(mosaic):,}"
    )

    print(
        f"OASST examples:        {len(oasst):,}"
    )

    print(
        f"Combined before merge:  "
        f"{len(mosaic) + len(oasst):,}"
    )

    # --------------------------------------------------------
    # Mosaic gets priority.
    #
    # OrderedDict preserves insertion order.
    # --------------------------------------------------------

    merged = OrderedDict()

    mosaic_duplicates = 0
    oasst_duplicates = 0

    for example in mosaic:

        key = normalize_question(
            example["user"]
        )

        if key in merged:

            mosaic_duplicates += 1
            continue

        merged[key] = example

    for example in oasst:

        key = normalize_question(
            example["user"]
        )

        if key in merged:

            oasst_duplicates += 1
            continue

        merged[key] = example

    final_examples = list(
        merged.values()
    )

    print()
    print(
        f"Duplicate Mosaic questions: "
        f"{mosaic_duplicates:,}"
    )

    print(
        f"OASST questions overlapping "
        f"with existing data: "
        f"{oasst_duplicates:,}"
    )

    print()
    print(
        f"Final examples: "
        f"{len(final_examples):,}"
    )

    # --------------------------------------------------------
    # Write output.
    # --------------------------------------------------------

    output = "\n\n".join(
        format_example(example)
        for example in final_examples
    )

    output += "\n"

    OUTPUT_FILE.write_text(
        output,
        encoding="utf-8"
    )

    print(
        f"Final characters: "
        f"{len(output):,}"
    )

    print(
        f"Saved: {OUTPUT_FILE}"
    )

    print()
    print("Merge complete.")


if __name__ == "__main__":
    main()
