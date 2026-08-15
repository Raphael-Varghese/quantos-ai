class CharacterTokenizer:

    def __init__(self, text):

        self.chars = sorted(set(text))

        self.vocab_size = len(self.chars)

        self.stoi = {
            character: index
            for index, character in enumerate(self.chars)
        }

        self.itos = {
            index: character
            for index, character in enumerate(self.chars)
        }

    def encode(self, text):

        return [
            self.stoi[character]
            for character in text
        ]

    def decode(self, tokens):

        return "".join(
            self.itos[token]
            for token in tokens
        )