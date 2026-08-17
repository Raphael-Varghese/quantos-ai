from pathlib import Path

from tokenizers import Tokenizer
from tokenizers.decoders import ByteLevel


TOKENIZER_FILE = Path(
    "data/processed/tokenizer/tokenizer.json"
)


class SubwordTokenizer:

    def __init__(
        self,
        tokenizer_file=TOKENIZER_FILE
    ):

        tokenizer_file = Path(
            tokenizer_file
        )

        if not tokenizer_file.exists():

            raise FileNotFoundError(
                f"Tokenizer not found: "
                f"{tokenizer_file}"
            )

        self.tokenizer = Tokenizer.from_file(
            str(tokenizer_file)
        )

        # Decode ByteLevel tokens correctly.
        self.tokenizer.decoder = ByteLevel()

        self.vocab_size = (
            self.tokenizer.get_vocab_size()
        )

    # ========================================================
    # Encode
    # ========================================================

    def encode(self, text):

        encoded = self.tokenizer.encode(
            text
        )

        return encoded.ids

    # ========================================================
    # Decode
    # ========================================================

    def decode(self, tokens):

        return self.tokenizer.decode(
            tokens,
            skip_special_tokens=False
        )

    # ========================================================
    # Token inspection
    # ========================================================

    def encode_with_tokens(self, text):

        encoded = self.tokenizer.encode(
            text
        )

        return (
            encoded.ids,
            encoded.tokens
        )