from pathlib import Path
import re


DATASET = Path("data/raw/train.txt")


def main():

    text = DATASET.read_text(
        encoding="utf-8"
    )

    examples = re.findall(
        r"<bos>\s*(.*?)\s*<end>",
        text,
        flags=re.DOTALL
    )

    print("=" * 70)
    print("MOSAIC DATASET VALIDATION")
    print("=" * 70)
    print()

    print(f"Raw characters: {len(text):,}")
    print(f"Examples found: {len(examples):,}")
    print()

    errors = []

    for index, example in enumerate(
        examples,
        start=1
    ):

        required = [
            "<system>",
            "<user>",
            "<assistant>",
        ]

        for marker in required:

            if marker not in example:

                errors.append(
                    (
                        index,
                        f"Missing {marker}"
                    )
                )

        system_pos = example.find("<system>")
        user_pos = example.find("<user>")
        assistant_pos = example.find("<assistant>")

        if not (
            system_pos < user_pos < assistant_pos
        ):

            errors.append(
                (
                    index,
                    "Incorrect section ordering"
                )
            )

    # Check for content outside records.
    reconstructed = "\n\n".join(
        f"<bos>\n{x}\n<end>"
        for x in examples
    )

    # This isn't an exact byte-for-byte comparison because whitespace
    # may differ, so just check structural counts.
    bos_count = text.count("<bos>")
    end_count = text.count("<end>")

    print(
        f"<bos> count:       {bos_count:,}"
    )

    print(
        f"<end> count:       {end_count:,}"
    )

    print()

    if bos_count != end_count:

        errors.append(
            (
                0,
                "<bos> and <end> counts do not match"
            )
        )

    if bos_count != len(examples):

        errors.append(
            (
                0,
                "<bos> count does not match parsed examples"
            )
        )

    if errors:

        print("VALIDATION FAILED")
        print()

        for index, message in errors[:50]:

            print(
                f"Example {index}: {message}"
            )

        print()
        print(
            f"Total errors: {len(errors):,}"
        )

        raise SystemExit(1)

    print("VALIDATION PASSED")
    print()
    print("Every example has:")
    print("  <bos>")
    print("  <system>")
    print("  <user>")
    print("  <assistant>")
    print("  <end>")


if __name__ == "__main__":
    main()
