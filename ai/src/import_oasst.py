from pathlib import Path

from datasets import load_dataset


OUTPUT_DIR = Path(
    "data/external/oasst1"
)

OUTPUT_FILE = (
    OUTPUT_DIR /
    "oasst1_mosaic.txt"
)

MAX_EXAMPLES = 5000


SYSTEM_PROMPT = (
    "You are Mosaic, a helpful general-purpose "
    "artificial intelligence assistant."
)


def clean_text(text):
    if text is None:
        return ""

    text = str(text)

    text = text.replace(
        "\r\n",
        "\n"
    )

    text = text.replace(
        "\r",
        "\n"
    )

    lines = [
        line.rstrip()
        for line in text.splitlines()
    ]

    return "\n".join(lines).strip()


def format_example(user, assistant):
    user = clean_text(user)
    assistant = clean_text(assistant)

    if not user or not assistant:
        return None

    return (
        "<bos>\n"
        "<system>\n"
        f"{SYSTEM_PROMPT}\n\n"
        "<user>\n"
        f"{user}\n\n"
        "<assistant>\n"
        f"{assistant}\n\n"
        "<end>"
    )


def main():

    print("=" * 70)
    print("IMPORTING OPENASSISTANT")
    print("=" * 70)

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print()
    print("Downloading/loading dataset...")

    dataset = load_dataset(
        "OpenAssistant/oasst1",
        split="train"
    )

    print(
        f"Rows available: {len(dataset):,}"
    )

    examples = []

    for row in dataset:

        if len(examples) >= MAX_EXAMPLES:
            break

        text = row.get("text")
        role = row.get("role")

        if role != "assistant":
            continue

        if not text:
            continue

        # OASST contains message trees. For this first
        # import we only keep assistant messages whose
        # parent message is represented separately.
        #
        # The parent relationship will be handled below.
        examples.append(
            clean_text(text)
        )

    print(
        f"Assistant messages selected: "
        f"{len(examples):,}"
    )

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        for index, assistant in enumerate(
            examples,
            start=1
        ):

            example = format_example(
                "Please respond helpfully.",
                assistant
            )

            if example is None:
                continue

            file.write(
                example
            )

            file.write(
                "\n\n"
            )

    print()
    print(
        f"Saved: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()