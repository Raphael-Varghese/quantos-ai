import torch

from .config import (
    TRAIN_FILE,
    TRAIN_SPLIT,
    BLOCK_SIZE,
    BATCH_SIZE,
    DEVICE,
)

from .tokenizer import CharacterTokenizer


class TextDataset:

    def __init__(self):

        with open(
            TRAIN_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            self.text = file.read()

        if len(self.text) < BLOCK_SIZE * 2:

            raise ValueError(
                "Your training file is too small. "
                f"Add at least {BLOCK_SIZE * 2} characters."
            )

        self.tokenizer = CharacterTokenizer(
            self.text
        )

        encoded = self.tokenizer.encode(
            self.text
        )

        self.data = torch.tensor(
            encoded,
            dtype=torch.long
        )

        split = int(
            len(self.data) * TRAIN_SPLIT
        )

        self.train_data = self.data[:split]

        self.validation_data = self.data[split:]

        print(
            f"Characters: {len(self.text):,}"
        )

        print(
            f"Vocabulary: {self.tokenizer.vocab_size:,}"
        )

        print(
            f"Training tokens: {len(self.train_data):,}"
        )

        print(
            f"Validation tokens: "
            f"{len(self.validation_data):,}"
        )

    def get_batch(self, split):

        if split == "train":

            data = self.train_data

        else:

            data = self.validation_data

        positions = torch.randint(
            0,
            len(data) - BLOCK_SIZE - 1,
            (BATCH_SIZE,)
        )

        x = torch.stack([
            data[i:i + BLOCK_SIZE]
            for i in positions
        ])

        y = torch.stack([
            data[i + 1:i + BLOCK_SIZE + 1]
            for i in positions
        ])

        return (
            x.to(DEVICE),
            y.to(DEVICE)
        )