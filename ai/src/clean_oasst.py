from pathlib import Path
from collections import defaultdict
import re


# ============================================================
# Configuration
# ============================================================

INPUT_FILE = Path(
    "data/external/oasst1/oasst1_mosaic.txt"
)

OUTPUT_FILE = Path(
    "data/external/oasst1/oasst1_clean.txt"
)

MIN_USER_CHARS = 10
MIN_ASSISTANT_CHARS = 80

MAX_USER_CHARS = 3000
MAX_ASSISTANT_CHARS = 3500

MIN_SCORE = 1


# ============================================================
# Parsing
# ============================================================

def parse_examples(text):

    examples = []

    chunks = text.split("<bos>")

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

        if not user or not assistant:
            continue

        examples.append(
            {
                "user": user,
                "assistant": assistant,
            }
        )

    return examples


# ============================================================
# Normalization
# ============================================================

def normalize_question(text):

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# Suspicious content
# ============================================================

SUSPICIOUS_PATTERNS = [

    # Requests for the assistant to pretend to be a person.
    r"\bpretend you are\b",
    r"\bact as if you are\b",
    r"\bif you were human\b",

    # Explicit model/personality bait.
    r"\bwhat(?:'s| is) your favorite\b",
    r"\bdo you have a favorite\b",

    # Conversation fragments rather than useful standalone questions.
    r"^\s*(please )?(continue|go on)\s*[.!?]*$",
    r"^\s*(ok|okay|thanks|thank you)\s*[.!?]*$",
    r"^\s*(can you elaborate|elaborate)\s*[.!?]*$",

    # Requests to reproduce hidden/internal information.
    r"\breveal (your|the) (system prompt|instructions)\b",
    r"\bshow (me )?(your|the) system prompt\b",
    r"\bhidden instructions\b",

]


def is_suspicious_question(question):

    normalized = normalize_question(
        question
    )

    for pattern in SUSPICIOUS_PATTERNS:

        if re.search(
            pattern,
            normalized
        ):
            return True

    return False


# ============================================================
# Quality scoring
# ============================================================

def score_answer(answer):

    score = 0

    length = len(answer)

    # Useful answer length.
    if length >= 200:
        score += 3

    elif length >= 120:
        score += 2

    elif length >= 80:
        score += 1

    # Multiple sentences generally indicate a developed answer.
    sentence_count = len(
        re.findall(
            r"[.!?](?:\s|$)",
            answer
        )
    )

    if sentence_count >= 3:
        score += 2

    elif sentence_count >= 2:
        score += 1

    # Structured response.
    if "\n" in answer:
        score += 1

    # Code examples.
    if (
        "```" in answer
        or "def " in answer
        or "return " in answer
    ):
        score += 1

    # Penalize obvious truncation.
    if answer.endswith(
        (
            ":",
            "...",
            "and",
            "or",
            "but",
        )
    ):
        score -= 3

    # Penalize unbalanced delimiters.
    if answer.count("(") > answer.count(")"):
        score -= 2

    if answer.count("{") > answer.count("}"):
        score -= 2

    if answer.count("[") > answer.count("]"):
        score -= 2

    return score


# ============================================================
# Formatting
# ============================================================

def format_example(user, assistant):

    system = (
        "You are Mosaic, a helpful general-purpose "
        "artificial intelligence assistant."
    )

    return (
        "<bos>\n"
        "<system>\n"
        f"{system}\n\n"
        "<user>\n"
        f"{user}\n\n"
        "<assistant>\n"
        f"{assistant}\n\n"
        "<end>"
    )


# ============================================================
# Main
# ============================================================

def main():

    print("=" * 70)
    print("CLEANING OPENASSISTANT")
    print("=" * 70)
    print()

    text = INPUT_FILE.read_text(
        encoding="utf-8"
    )

    examples = parse_examples(text)

    print(
        f"Input examples: "
        f"{len(examples):,}"
    )

    # --------------------------------------------------------
    # Length filtering
    # --------------------------------------------------------

    filtered = []

    rejected_length = 0

    for example in examples:

        user = example["user"]
        assistant = example["assistant"]

        if len(user) < MIN_USER_CHARS:
            rejected_length += 1
            continue

        if len(user) > MAX_USER_CHARS:
            rejected_length += 1
            continue

        if len(assistant) < MIN_ASSISTANT_CHARS:
            rejected_length += 1
            continue

        if len(assistant) > MAX_ASSISTANT_CHARS:
            rejected_length += 1
            continue

        filtered.append(
            example
        )

    print(
        f"After length filtering: "
        f"{len(filtered):,}"
    )

    print(
        f"Rejected by length: "
        f"{rejected_length:,}"
    )

    # --------------------------------------------------------
    # Suspicious question filtering
    # --------------------------------------------------------

    clean = []

    rejected_suspicious = 0

    for example in filtered:

        if is_suspicious_question(
            example["user"]
        ):
            rejected_suspicious += 1
            continue

        clean.append(
            example
        )

    print(
        f"After suspicious filtering: "
        f"{len(clean):,}"
    )

    print(
        f"Rejected as suspicious: "
        f"{rejected_suspicious:,}"
    )

    # --------------------------------------------------------
    # Group by normalized question.
    # --------------------------------------------------------

    groups = defaultdict(list)

    for example in clean:

        key = normalize_question(
            example["user"]
        )

        groups[key].append(
            example
        )

    print(
        f"Unique questions: "
        f"{len(groups):,}"
    )

    # --------------------------------------------------------
    # Select highest-quality answer.
    # --------------------------------------------------------

    selected = []

    rejected_low_score = 0

    for question, candidates in groups.items():

        best = max(
            candidates,
            key=lambda x: score_answer(
                x["assistant"]
            )
        )

        score = score_answer(
            best["assistant"]
        )

        if score < MIN_SCORE:

            rejected_low_score += 1
            continue

        selected.append(
            best
        )

    print(
        f"Rejected low-score examples: "
        f"{rejected_low_score:,}"
    )

    # --------------------------------------------------------
    # Deterministic ordering.
    # --------------------------------------------------------

    selected.sort(
        key=lambda x: normalize_question(
            x["user"]
        )
    )

    # --------------------------------------------------------
    # Format.
    # --------------------------------------------------------

    output = "\n\n".join(
        format_example(
            x["user"],
            x["assistant"]
        )
        for x in selected
    )

    output += "\n"

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        output,
        encoding="utf-8"
    )

    print()
    print(
        f"Final examples: "
        f"{len(selected):,}"
    )

    print(
        f"Final characters: "
        f"{len(output):,}"
    )

    print(
        f"Saved: {OUTPUT_FILE}"
    )

    print()
    print("Cleaning complete.")


if __name__ == "__main__":
    main()