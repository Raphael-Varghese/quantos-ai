import torch

from .config import (
    DEVICE,
    CHECKPOINT_FILE,
)

from .model import GPT
from .subword_tokenizer import SubwordTokenizer


# ============================================================
# Load checkpoint
# ============================================================

print("Loading model...")

checkpoint = torch.load(
    CHECKPOINT_FILE,
    map_location=DEVICE,
    weights_only=False
)

vocab_size = checkpoint["vocab_size"]


# ============================================================
# Tokenizer
# ============================================================

tokenizer = SubwordTokenizer()

print("Tokenizer loaded.")
print(
    f"Vocabulary size: {tokenizer.vocab_size}"
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

    if prompt.lower().strip() == "exit":

        break

    if not prompt.strip():

        continue


    # --------------------------------------------------------
    # Build conversation prompt
    # --------------------------------------------------------

    formatted_prompt = (
        "<bos>\n"
        "<system>\n"
        "You are Mosaic, a helpful general-purpose artificial "
        "intelligence assistant.\n\n"
        "<user>\n"
        f"{prompt}\n\n"
        "<assistant>\n"
    )


    # --------------------------------------------------------
    # Tokenize
    # --------------------------------------------------------

    encoded = tokenizer.encode(
        formatted_prompt
    )

    tokens = torch.tensor(
        [encoded],
        dtype=torch.long,
        device=DEVICE
    )


    # --------------------------------------------------------
    # Generate
    # --------------------------------------------------------

    with torch.no_grad():

        generated = model.generate(
            tokens,
            max_new_tokens=100,
            temperature=0.8,
            top_k=40
        )


    # --------------------------------------------------------
    # Get newly generated tokens
    # --------------------------------------------------------

    new_tokens = generated[
        0,
        len(encoded):
    ].tolist()


    # --------------------------------------------------------
    # Stop at <end>
    # --------------------------------------------------------

    end_tokens = tokenizer.encode(
        "<end>"
    )

    end_length = len(end_tokens)

    for i in range(
        len(new_tokens) - end_length + 1
    ):

        if (
            new_tokens[
                i:i + end_length
            ]
            ==
            end_tokens
        ):

            new_tokens = new_tokens[:i]

            break


    # --------------------------------------------------------
    # Decode
    # --------------------------------------------------------

    response = tokenizer.decode(
        new_tokens
    )


    print()
    print("AI:", response.strip())
    print()