import sys

import torch

from .config import (
    DEVICE,
    CHECKPOINT_FILE,
)

from .model import GPT


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

stoi = checkpoint[
    "tokenizer_stoi"
]

itos = checkpoint[
    "tokenizer_itos"
]


# ============================================================
# Tokenizer functions
# ============================================================

def encode(text):

    tokens = []

    for character in text:

        if character in stoi:

            tokens.append(
                stoi[character]
            )

    return tokens


def decode(tokens):

    return "".join(
        itos[token]
        for token in tokens
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


print("Model loaded.")
print()
print("Type 'exit' to quit.")
print()


# ============================================================
# Chat loop
# ============================================================

while True:

    prompt = input("You: ")

    if prompt.lower() == "exit":

        break

    if not prompt.strip():

        continue

    encoded = encode(prompt)

    if not encoded:

        print(
            "I don't recognize those characters."
        )

        continue

    tokens = torch.tensor(
        [encoded],
        dtype=torch.long,
        device=DEVICE
    )

    generated = model.generate(
        tokens,
        max_new_tokens=200,
        temperature=0.8,
        top_k=40
    )

    new_tokens = generated[
        0
    ].tolist()

    response = decode(
        new_tokens
    )

    print()
    print("AI:", response)
    print()