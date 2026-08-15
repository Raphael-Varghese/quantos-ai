import numpy as np
import torch

from .config import (
    BLOCK_SIZE,
    BATCH_SIZE,
    DEVICE,
)


# ============================================================
# Dataset
# ============================================================

class TextDataset:

    def __init__(self):

        train_path = (
            "data/processed/train.bin"
        )

        validation_path = (
            "data/processed/val.bin"
        )

        # ----------------------------------------------------
        # Load binary token data
        # ----------------------------------------------------

        self.train_data = torch.from_numpy(
            np.fromfile(
                train_path,
                dtype=np.uint16
            ).astype(np.int64)
        )

        self.validation_data = torch.from_numpy(
            np.fromfile(
                validation_path,
                dtype=np.uint16
            ).astype(np.int64)
        )

        # ----------------------------------------------------
        # Validate dataset size
        # ----------------------------------------------------

        minimum_tokens = (
            BLOCK_SIZE + 1
        )

        if len(self.train_data) < minimum_tokens:

            raise ValueError(
                "Training dataset is too small. "
                f"Need at least {minimum_tokens} "
                f"tokens, got {len(self.train_data)}."
            )

        if len(self.validation_data) < minimum_tokens:

            raise ValueError(
                "Validation dataset is too small. "
                f"Need at least {minimum_tokens} "
                f"tokens, got "
                f"{len(self.validation_data)}."
            )

        # ----------------------------------------------------
        # Information
        # ----------------------------------------------------

        print(
            f"Training tokens: "
            f"{len(self.train_data):,}"
        )

        print(
            f"Validation tokens: "
            f"{len(self.validation_data):,}"
        )

    # ========================================================
    # Batch
    # ========================================================

    def get_batch(self, split):

        if split == "train":

            data = self.train_data

        elif split == "validation":

            data = self.validation_data

        else:

            raise ValueError(
                f"Unknown split: {split}"
            )

        # ----------------------------------------------------
        # Random positions
        # ----------------------------------------------------

        max_position = (
            len(data)
            - BLOCK_SIZE
            - 1
        )

        positions = torch.randint(
            0,
            max_position + 1,
            (BATCH_SIZE,)
        )

        # ----------------------------------------------------
        # Vectorized sequence construction
        # ----------------------------------------------------

        offsets = torch.arange(
            BLOCK_SIZE
        )

        indices = (
            positions[:, None]
            +
            offsets[None, :]
        )

        x = data[
            indices
        ]

        y = data[
            indices + 1
        ]

        return (
            x.to(DEVICE),
            y.to(DEVICE)
        )