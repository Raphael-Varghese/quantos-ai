from .subword_tokenizer import (
    SubwordTokenizer
)


tokenizer = SubwordTokenizer()


text = (
    "The quick brown fox jumps over the lazy dog. "
    "I am a test sentence for the tokenizer. "
    "This is a longer sentence to test the tokenizer's ability to handle more complex input. "
    "Let's see how well it performs with this text."
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