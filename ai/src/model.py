import torch
import torch.nn as nn
import torch.nn.functional as F

from .config import (
    BLOCK_SIZE,
    EMBEDDING_SIZE,
    NUM_HEADS,
    NUM_LAYERS,
    DROPOUT,
)


# ============================================================
# Attention Head
# ============================================================

class AttentionHead(nn.Module):

    def __init__(self, head_size):

        super().__init__()

        self.key = nn.Linear(
            EMBEDDING_SIZE,
            head_size,
            bias=False
        )

        self.query = nn.Linear(
            EMBEDDING_SIZE,
            head_size,
            bias=False
        )

        self.value = nn.Linear(
            EMBEDDING_SIZE,
            head_size,
            bias=False
        )

        self.dropout = nn.Dropout(
            DROPOUT
        )

        self.register_buffer(
            "mask",
            torch.tril(
                torch.ones(
                    BLOCK_SIZE,
                    BLOCK_SIZE
                )
            )
        )

    def forward(self, x):

        batch, tokens, channels = x.shape

        key = self.key(x)

        query = self.query(x)

        value = self.value(x)

        # Attention scores
        scores = (
            query @ key.transpose(-2, -1)
        )

        scores = scores / (
            key.shape[-1] ** 0.5
        )

        # Causal masking.
        # The model cannot look into the future.
        scores = scores.masked_fill(
            self.mask[:tokens, :tokens] == 0,
            float("-inf")
        )

        weights = F.softmax(
            scores,
            dim=-1
        )

        weights = self.dropout(weights)

        output = weights @ value

        return output


# ============================================================
# Multi-head attention
# ============================================================

class MultiHeadAttention(nn.Module):

    def __init__(self):

        super().__init__()

        head_size = (
            EMBEDDING_SIZE // NUM_HEADS
        )

        self.heads = nn.ModuleList([
            AttentionHead(head_size)
            for _ in range(NUM_HEADS)
        ])

        self.projection = nn.Linear(
            EMBEDDING_SIZE,
            EMBEDDING_SIZE
        )

        self.dropout = nn.Dropout(
            DROPOUT
        )

    def forward(self, x):

        output = torch.cat(
            [
                head(x)
                for head in self.heads
            ],
            dim=-1
        )

        output = self.projection(output)

        output = self.dropout(output)

        return output


# ============================================================
# Feed Forward Network
# ============================================================

class FeedForward(nn.Module):

    def __init__(self):

        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(
                EMBEDDING_SIZE,
                EMBEDDING_SIZE * 4
            ),

            nn.GELU(),

            nn.Linear(
                EMBEDDING_SIZE * 4,
                EMBEDDING_SIZE
            ),

            nn.Dropout(DROPOUT)
        )

    def forward(self, x):

        return self.network(x)


# ============================================================
# Transformer Block
# ============================================================

class TransformerBlock(nn.Module):

    def __init__(self):

        super().__init__()

        self.attention = (
            MultiHeadAttention()
        )

        self.feed_forward = (
            FeedForward()
        )

        self.layer_norm_1 = (
            nn.LayerNorm(EMBEDDING_SIZE)
        )

        self.layer_norm_2 = (
            nn.LayerNorm(EMBEDDING_SIZE)
        )

    def forward(self, x):

        # Attention
        x = x + self.attention(
            self.layer_norm_1(x)
        )

        # Feed-forward
        x = x + self.feed_forward(
            self.layer_norm_2(x)
        )

        return x


# ============================================================
# GPT
# ============================================================

class GPT(nn.Module):

    def __init__(self, vocab_size):

        super().__init__()

        self.vocab_size = vocab_size

        # Token embedding
        self.token_embedding = nn.Embedding(
            vocab_size,
            EMBEDDING_SIZE
        )

        # Position embedding
        self.position_embedding = nn.Embedding(
            BLOCK_SIZE,
            EMBEDDING_SIZE
        )

        # Transformer
        self.blocks = nn.Sequential(
            *[
                TransformerBlock()
                for _ in range(NUM_LAYERS)
            ]
        )

        # Final normalization
        self.final_norm = nn.LayerNorm(
            EMBEDDING_SIZE
        )

        # Language-model output
        self.output = nn.Linear(
            EMBEDDING_SIZE,
            vocab_size
        )

        self.apply(self._initialize_weights)

    def _initialize_weights(self, module):

        if isinstance(module, nn.Linear):

            nn.init.normal_(
                module.weight,
                mean=0.0,
                std=0.02
            )

            if module.bias is not None:

                nn.init.zeros_(
                    module.bias
                )

        elif isinstance(module, nn.Embedding):

            nn.init.normal_(
                module.weight,
                mean=0.0,
                std=0.02
            )

    def forward(self, tokens, targets=None):

        batch, sequence_length = tokens.shape

        positions = torch.arange(
            sequence_length,
            device=tokens.device
        )

        # Token + positional information
        x = (
            self.token_embedding(tokens)
            +
            self.position_embedding(positions)
        )

        # Transformer
        x = self.blocks(x)

        x = self.final_norm(x)

        # Vocabulary logits
        logits = self.output(x)

        loss = None

        if targets is not None:

            batch, sequence, vocabulary = (
                logits.shape
            )

            logits = logits.reshape(
                batch * sequence,
                vocabulary
            )

            targets = targets.reshape(
                batch * sequence
            )

            loss = F.cross_entropy(
                logits,
                targets
            )

        return logits, loss

    @torch.no_grad()
    def generate(
        self,
        tokens,
        max_new_tokens=200,
        temperature=0.8,
        top_k=40
    ):

        for _ in range(max_new_tokens):

            # Keep context within model limit
            context = tokens[:, -BLOCK_SIZE:]

            logits, _ = self(context)

            # Only predict next token
            logits = logits[:, -1, :]

            logits = (
                logits / temperature
            )

            # Top-k sampling
            if top_k is not None:

                values, _ = torch.topk(
                    logits,
                    min(
                        top_k,
                        logits.shape[-1]
                    )
                )

                threshold = values[:, [-1]]

                logits = logits.masked_fill(
                    logits < threshold,
                    float("-inf")
                )

            probabilities = F.softmax(
                logits,
                dim=-1
            )

            next_token = torch.multinomial(
                probabilities,
                num_samples=1
            )

            tokens = torch.cat(
                [
                    tokens,
                    next_token
                ],
                dim=1
            )

        return tokens