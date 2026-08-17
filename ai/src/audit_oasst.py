from pathlib import Path
from collections import Counter
import re


INPUT_FILE = Path(
    "data/external/oasst1/oasst1_mosaic.txt"
)


def parse_examples(text):

    chunks = text.split("<bos>")

    examples = []

    for chunk in chunks:

        chunk = chunk.strip()

        if not chunk:
            continue

        if "<user>" not in chunk:
            continue

        if "<assistant>" not in chunk:
            continue

        if "<end>" not in chunk:
            continue

        user = chunk.split(
            "<user>",
            1
        )[1].split(
            "<assistant>",
            1
        )[0].strip()

        assistant = chunk.split(
            "<assistant>",
            1
        )[1].split(
            "<end>",
            1
        )[0].strip()

        examples.append(
            {
                "user": user,
                "assistant": assistant,
            }
        )

    return examples


def normalize_question(text):

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def main():

    text = INPUT_FILE.read_text(
        encoding="utf-8"
    )

    examples = parse_examples(text)

    print("=" * 70)
    print("OPENASSISTANT DATASET AUDIT")
    print("=" * 70)
    print()

    print(
        f"Examples: {len(examples):,}"
    )

    print()

    # --------------------------------------------------------
    # Question duplicates
    # --------------------------------------------------------

    questions = Counter(
        normalize_question(
            x["user"]
        )
        for x in examples
    )

    duplicate_questions = [
        (question, count)
        for question, count
        in questions.items()
        if count > 1
    ]

    duplicate_questions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print(
        f"Unique questions: "
        f"{len(questions):,}"
    )

    print(
        f"Duplicate questions: "
        f"{len(duplicate_questions):,}"
    )

    print()

    print("Top duplicate questions:")

    for question, count in duplicate_questions[:30]:

        print(
            f"  {count:3d}x "
            f"{question[:120]}"
        )

    # --------------------------------------------------------
    # Length statistics
    # --------------------------------------------------------

    user_lengths = [
        len(x["user"])
        for x in examples
    ]

    assistant_lengths = [
        len(x["assistant"])
        for x in examples
    ]

    print()
    print("=" * 70)
    print("LENGTH STATISTICS")
    print("=" * 70)

    print(
        f"User min:        {min(user_lengths):,}"
    )

    print(
        f"User max:        {max(user_lengths):,}"
    )

    print(
        f"Assistant min:   {min(assistant_lengths):,}"
    )

    print(
        f"Assistant max:   {max(assistant_lengths):,}"
    )

    print()

    # --------------------------------------------------------
    # Suspicious prompts
    # --------------------------------------------------------

    suspicious_prompts = [
        "please respond helpfully",
        "please answer helpfully",
        "respond helpfully",
        "answer helpfully",
    ]

    suspicious = []

    for example in examples:

        question = normalize_question(
            example["user"]
        )

        for phrase in suspicious_prompts:

            if question == phrase:

                suspicious.append(
                    example
                )

                break

    print(
        f"Generic/suspicious prompts: "
        f"{len(suspicious):,}"
    )

    # --------------------------------------------------------
    # Very short answers
    # --------------------------------------------------------

    short_answers = [
        x
        for x in examples
        if len(x["assistant"]) < 80
    ]

    print(
        f"Answers under 80 chars: "
        f"{len(short_answers):,}"
    )

    # --------------------------------------------------------
    # Very long answers
    # --------------------------------------------------------

    long_answers = [
        x
        for x in examples
        if len(x["assistant"]) > 3500
    ]

    print(
        f"Answers over 3,500 chars: "
        f"{len(long_answers):,}"
    )

    # --------------------------------------------------------
    # Empty / malformed
    # --------------------------------------------------------

    malformed = [
        x
        for x in examples
        if not x["user"]
        or not x["assistant"]
    ]

    print(
        f"Malformed examples: "
        f"{len(malformed):,}"
    )

    print()
    print("=" * 70)
    print("AUDIT COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()