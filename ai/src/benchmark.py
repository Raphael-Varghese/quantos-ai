from pathlib import Path

import torch

from .config import (
    DEVICE,
    CHECKPOINT_FILE,
)

from .model import GPT
from .subword_tokenizer import SubwordTokenizer


# ============================================================
# Configuration
# ============================================================

EVAL_DIR = Path(
    "data/eval"
)

MAX_NEW_TOKENS = 100

TEMPERATURE = 0.7

TOP_K = 40


# ============================================================
# Load checkpoint
# ============================================================

print("Loading model...")

checkpoint = torch.load(
    CHECKPOINT_FILE,
    map_location=DEVICE,
    weights_only=False
)

vocab_size = checkpoint[
    "vocab_size"
]


# ============================================================
# Tokenizer
# ============================================================

tokenizer = SubwordTokenizer()

print(
    f"Tokenizer vocabulary: "
    f"{tokenizer.vocab_size:,}"
)

print(
    f"Model vocabulary: "
    f"{vocab_size:,}"
)

if tokenizer.vocab_size != vocab_size:

    raise ValueError(
        "Tokenizer vocabulary does not match "
        "the model vocabulary."
    )


# ============================================================
# Model
# ============================================================

model = GPT(
    vocab_size
).to(DEVICE)

model.load_state_dict(
    checkpoint["model"]
)

model.eval()


# ============================================================
# Evaluation files
# ============================================================

files = sorted(
    EVAL_DIR.glob("*.txt")
)

if not files:

    raise FileNotFoundError(
        f"No evaluation files found in {EVAL_DIR}"
    )


# ============================================================
# Parse questions
# ============================================================

def load_questions(path):

    text = path.read_text(
        encoding="utf-8"
    )

    questions = []

    current = None

    for line in text.splitlines():

        line = line.strip()

        if line == "<question>":

            if current:

                questions.append(
                    current.strip()
                )

            current = ""

            continue

        if current is not None:

            current += line + "\n"


    if current:

        questions.append(
            current.strip()
        )

    return questions


# ============================================================
# Generate
# ============================================================

def generate_answer(question):

    prompt = (
        "<bos>\n"
        "<system>\n"
        "You are Mosaic, a helpful general-purpose "
        "artificial intelligence assistant.\n\n"
        "<user>\n"
        f"{question}\n\n"
        "<assistant>\n"
    )

    encoded = tokenizer.encode(
        prompt
    )

    tokens = torch.tensor(
        [encoded],
        dtype=torch.long,
        device=DEVICE
    )

    with torch.no_grad():

        generated = model.generate(
            tokens,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            top_k=TOP_K
        )

    new_tokens = generated[
        0,
        len(encoded):
    ].tolist()

    response = tokenizer.decode(
        new_tokens
    )

    # Stop at <end> if generated.
    end_position = response.find(
        "<end>"
    )

    if end_position != -1:

        response = response[
            :end_position
        ]

    return response.strip()


# ============================================================
# Run benchmark
# ============================================================

print()
print("=" * 60)
print("MOSAIC BENCHMARK")
print("=" * 60)

print(
    f"Checkpoint: {CHECKPOINT_FILE}"
)

print(
    f"Training step: "
    f"{checkpoint.get('step', 'unknown')}"
)

print()


for path in files:

    category = path.stem

    questions = load_questions(
        path
    )

    print()
    print(
        "=" * 60
    )

    print(
        f"CATEGORY: {category.upper()}"
    )

    print(
        f"Questions: {len(questions)}"
    )

    print(
        "=" * 60
    )

    for index, question in enumerate(
        questions,
        start=1
    ):

        print()
        print(
            f"[{index}/{len(questions)}]"
        )

        print(
            f"USER: {question}"
        )

        answer = generate_answer(
            question
        )

        print()

        print(
            f"MOSAIC: {answer}"
        )

        print()