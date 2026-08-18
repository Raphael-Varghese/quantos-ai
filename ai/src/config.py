import os
import torch


# ============================================================
# Hardware
# ============================================================

DEVICE = torch.device("cpu")

CPU_COUNT = min(
    os.cpu_count() or 4,
    4
)

torch.set_num_threads(CPU_COUNT)


# ============================================================
# Reproducibility
# ============================================================

SEED = 1337


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

MAX_STEPS = 5000

LEARNING_RATE = 3e-4

MIN_LEARNING_RATE = 3e-5

WARMUP_STEPS = 250

WEIGHT_DECAY = 0.1

GRADIENT_CLIP = 1.0


# ============================================================
# Evaluation
# ============================================================

EVAL_INTERVAL = 100

EVAL_STEPS = 20


# ============================================================
# Saving
# ============================================================

CHECKPOINT_DIR = "checkpoints"

CHECKPOINT_FILE = (
    f"{CHECKPOINT_DIR}/model.pt"
)

RESUME_FROM_CHECKPOINT = True