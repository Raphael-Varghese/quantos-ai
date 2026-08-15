import os
import torch


# ============================================================
# Hardware
# ============================================================

DEVICE = torch.device("cpu")

CPU_COUNT = os.cpu_count() or 4

# Don't necessarily use every available CPU thread.
torch.set_num_threads(CPU_COUNT)


# ============================================================
# Dataset
# ============================================================

TRAIN_FILE = "data/raw/train.txt"

TRAIN_SPLIT = 0.90


# ============================================================
# Model
# ============================================================

BLOCK_SIZE = 256

VOCAB_SIZE = None

EMBEDDING_SIZE = 256

NUM_HEADS = 4

NUM_LAYERS = 4

DROPOUT = 0.1


# ============================================================
# Training
# ============================================================

BATCH_SIZE = 8

GRADIENT_ACCUMULATION_STEPS = 4

LEARNING_RATE = 3e-4

WEIGHT_DECAY = 0.1

MAX_STEPS = 5000

EVAL_INTERVAL = 250

EVAL_STEPS = 50

GRADIENT_CLIP = 1.0


# ============================================================
# Saving
# ============================================================

CHECKPOINT_DIR = "checkpoints"

CHECKPOINT_FILE = (
    f"{CHECKPOINT_DIR}/model.pt"
)