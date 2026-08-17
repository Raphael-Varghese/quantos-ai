from pathlib import Path

from datasets import load_dataset


OUTPUT_DIR = Path("data/external/oasst1")
OUTPUT_FILE = OUTPUT_DIR / "oasst1_mosaic.txt"

MAX_EXAMPLES = 5000

MIN_USER_CHARS = 10
MIN_ASSISTANT_CHARS = 40
MAX_ASSISTANT_CHARS = 4000


SYSTEM_PROMPT = (
    "You are Mosaic, a helpful general-purpose artificial "
    "intelligence assistant."
)


def clean_text(text):
    if not isinstance(text, str):
        return ""

    return (
        text
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .strip()
    )


def format_example(user, assistant):
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
    print()

    print("Downloading/loading dataset...")

    dataset = load_dataset(
        "OpenAssistant/oasst1",
        split="train"
    )

    print(
        f"Rows available: {len(dataset):,}"
    )

    # --------------------------------------------------------
    # Build message index.
    # --------------------------------------------------------

    messages = {}

    for row in dataset:

        message_id = row.get("message_id")

        if message_id:
            messages[message_id] = row

    print(
        f"Indexed messages: {len(messages):,}"
    )

    # --------------------------------------------------------
    # Extract assistant responses with their parent prompt.
    # --------------------------------------------------------

    examples = []

    seen = set()

    for row in dataset:

        if row.get("deleted", False):
            continue

        if row.get("role") != "assistant":
            continue

        if row.get("lang") not in (None, "en"):
            continue

        assistant = clean_text(
            row.get("text", "")
        )

        if len(assistant) < MIN_ASSISTANT_CHARS:
            continue

        if len(assistant) > MAX_ASSISTANT_CHARS:
            continue

        parent_id = row.get("parent_id")

        if not parent_id:
            continue

        parent = messages.get(parent_id)

        if parent is None:
            continue

        if parent.get("deleted", False):
            continue

        if parent.get("role") != "prompter":
            continue

        if parent.get("lang") not in (None, "en"):
            continue

        user = clean_text(
            parent.get("text", "")
        )

        if len(user) < MIN_USER_CHARS:
            continue

        key = (
            user,
            assistant
        )

        if key in seen:
            continue

        seen.add(key)

        examples.append(
            format_example(
                user,
                assistant
            )
        )

        if len(examples) >= MAX_EXAMPLES:
            break

    if not examples:
        raise RuntimeError(
            "No valid OpenAssistant examples found."
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        "\n\n".join(examples) + "\n",
        encoding="utf-8"
    )

    print()
    print(
        f"Examples selected: {len(examples):,}"
    )

    print(
        f"Saved: {OUTPUT_FILE}"
    )

    print()
    print("Import complete.")


if __name__ == "__main__":
    main()