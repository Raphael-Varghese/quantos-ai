from .subword_tokenizer import (
    SubwordTokenizer
)


tokenizer = SubwordTokenizer()


text = (
    "Write a paragraph about the"
    " importance of tokenization in natural language."
)


ids, tokens = (
    tokenizer.encode_with_tokens(
        text
    )
)


print(
    f"Vocabulary size: "
    f"{tokenizer.vocab_size}"
)

print()

print(
    "Tokens:"
)

print(
    tokens
)

print()

print(
    "IDs:"
)

print(
    ids
)

print()

decoded = tokenizer.decode(
    ids
)

print(
    "Decoded:"
)

print(
    decoded
)

print()

if decoded == text:

    print(
        "Round-trip test: PASS"
    )

else:

    print(
        "Round-trip test: FAIL"
    )