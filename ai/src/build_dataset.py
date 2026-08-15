from pathlib import Path
import random


OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# General knowledge
# ============================================================

knowledge = [

"""
TOPIC: Artificial Intelligence

Artificial intelligence is the field of creating computer systems that
perform tasks commonly associated with intelligence.

Machine learning is a subset of artificial intelligence in which a model
learns patterns from data.

Deep learning is a type of machine learning based on neural networks with
multiple computational layers.

A language model predicts tokens based on previous tokens.

A Transformer is a neural network architecture based heavily on attention
mechanisms.

Attention allows a model to assign different importance to different parts
of an input sequence.

A neural network contains parameters whose values are adjusted during
training.

Training generally involves making predictions, calculating a loss, and
using gradients to update parameters.
""",

"""
TOPIC: Python

Python is a general-purpose programming language.

Variables hold references to values.

Functions allow reusable operations to be defined.

Classes provide a mechanism for organizing data and behavior.

Lists are ordered mutable collections.

Tuples are ordered immutable collections.

Dictionaries store key-value associations.

Sets store unique elements.

A Python program can be divided into modules and packages.

Exceptions provide a mechanism for handling errors.

The Python interpreter executes Python programs.
""",

"""
TOPIC: Neural Networks

A neural network transforms input representations through a sequence of
mathematical operations.

A linear layer performs a matrix multiplication followed by an optional
bias addition.

An activation function introduces nonlinearity.

ReLU, GELU, sigmoid, and tanh are examples of activation functions.

A loss function measures how different a model prediction is from a target.

Backpropagation calculates gradients of the loss with respect to model
parameters.

An optimizer uses those gradients to update parameters.

Adam and AdamW are commonly used optimizers for neural network training.
""",

"""
TOPIC: Transformers

A Transformer processes sequences using attention and feed-forward layers.

Self-attention allows each token representation to interact with other
tokens in the sequence.

Queries, keys, and values are used to calculate attention.

Attention scores are commonly scaled by the square root of the key
dimension.

Softmax converts attention scores into normalized weights.

Multi-head attention performs several attention operations in parallel.

Residual connections help information flow through deep networks.

Layer normalization stabilizes neural network computation.

A causal language model prevents a token from attending to future tokens.

GPT-style models are autoregressive causal language models.
""",

"""
TOPIC: Training

Training a neural network means optimizing its parameters using data.

A batch is a collection of training examples processed together.

An epoch represents a complete pass through a dataset.

The learning rate controls the size of parameter updates.

Weight decay can regularize model parameters.

Gradient clipping limits excessively large gradients.

A validation set can be used to measure performance on data not directly
used for parameter updates.

Overfitting occurs when a model becomes excessively specialized to its
training examples.

Underfitting occurs when a model is unable to capture important patterns
in its training data.
"""
]


# ============================================================
# Conversations
# ============================================================

conversations = [

"""
SYSTEM: You are a helpful AI assistant.

USER: What is a neural network?

ASSISTANT: A neural network is a mathematical model made from connected
computational layers. During training, its parameters are adjusted so that
the network learns useful patterns from examples.
""",

"""
SYSTEM: You are a helpful AI assistant.

USER: What is a Transformer?

ASSISTANT: A Transformer is a neural network architecture that uses attention
mechanisms to process relationships between elements in a sequence. Modern
language models commonly use Transformer architectures.
""",

"""
SYSTEM: You are a helpful AI assistant.

USER: Explain attention simply.

ASSISTANT: Attention lets the model decide which parts of the available
context are most relevant when producing a particular representation.

For example, when interpreting a sentence, a word can use information from
other words that are especially relevant to its meaning.
""",

"""
SYSTEM: You are a helpful AI assistant.

USER: What is overfitting?

ASSISTANT: Overfitting happens when a model learns the training examples too
specifically and performs worse on new examples. One common sign is that
training loss continues to improve while validation performance stops
improving or becomes worse.
""",

"""
SYSTEM: You are a helpful AI assistant.

USER: Why does a language model need a tokenizer?

ASSISTANT: Neural networks operate on numerical representations. A tokenizer
converts text into discrete tokens, which can then be converted into
numbers and processed by the model.
"""
]


# ============================================================
# Instruction following
# ============================================================

instructions = [

"""
SYSTEM: Follow the user's instructions carefully.

USER: Give me three benefits of exercise.

ASSISTANT:
1. Exercise can improve cardiovascular fitness.
2. Exercise can improve muscular strength and endurance.
3. Regular physical activity can support overall health.
""",

"""
SYSTEM: Follow the user's instructions carefully.

USER: Explain recursion in one paragraph.

ASSISTANT: Recursion is a programming technique in which a function calls
itself to solve smaller versions of the same problem. A recursive function
needs a base case that stops the recursion and a recursive case that moves
the problem toward that base case.
""",

"""
SYSTEM: Follow the user's instructions carefully.

USER: Give me a concise definition of an API.

ASSISTANT: An API is an interface that allows software components to
communicate with each other through defined operations and data formats.
""",

"""
SYSTEM: Follow the user's instructions carefully.

USER: Turn this idea into three bullet points: neural networks learn from
examples.

ASSISTANT:
- Neural networks process training examples.
- Training adjusts model parameters.
- The model learns statistical patterns from the examples.
"""
]


# ============================================================
# Programming examples
# ============================================================

coding = [

"""
SYSTEM: You are an expert Python programming assistant.

USER: Write a function that adds two numbers.

ASSISTANT:

def add(a, b):
    return a + b
""",

"""
SYSTEM: You are an expert Python programming assistant.

USER: Write a function that checks whether a number is even.

ASSISTANT:

def is_even(number):
    return number % 2 == 0
""",

"""
SYSTEM: You are an expert Python programming assistant.

USER: How do I read a text file in Python?

ASSISTANT:

with open("file.txt", "r", encoding="utf-8") as file:
    text = file.read()

The with statement automatically closes the file when the block finishes.
""",

"""
SYSTEM: You are an expert Python programming assistant.

USER: What is a Python dictionary?

ASSISTANT: A dictionary is a mutable collection that associates keys with
values.

Example:

person = {
    "name": "Alex",
    "age": 25
}

The value associated with a key can be accessed with dictionary[key].
"""
]


# ============================================================
# Reasoning examples
# ============================================================

reasoning = [

"""
SYSTEM: Solve the problem carefully.

USER: If a box contains 5 groups of 8 objects, how many objects are there?

ASSISTANT: There are 5 groups and each group contains 8 objects.

5 × 8 = 40.

Therefore, there are 40 objects.
""",

"""
SYSTEM: Solve the problem carefully.

USER: A program processes 100 records in 5 seconds. Assuming constant
processing speed, how many records can it process in 20 seconds?

ASSISTANT: 20 seconds is four times 5 seconds.

100 × 4 = 400.

Therefore, the program can process approximately 400 records in 20 seconds
under the stated assumption.
""",

"""
SYSTEM: Solve the problem carefully.

USER: Why might increasing model size not always improve a model?

ASSISTANT: Larger models generally provide more representational capacity,
but size alone does not guarantee better results. Performance also depends
on training data quality, quantity, optimization, architecture, training
compute, and evaluation. A larger model trained poorly can perform worse
than a smaller well-trained model.
"""
]


# ============================================================
# Error correction
# ============================================================

corrections = [

"""
SYSTEM: Correct factual mistakes politely.

USER: Python is a compiled language just like C.

ASSISTANT: Python implementations commonly execute Python source through an
interpreter or runtime system, although some implementations use compilation
steps internally. It is therefore more accurate to describe Python as a
high-level language with multiple implementation strategies rather than
simply calling it identical to C's traditional compilation model.
""",

"""
SYSTEM: Correct factual mistakes politely.

USER: A Transformer does not use neural networks.

ASSISTANT: A Transformer is itself a neural network architecture. It uses
components such as attention mechanisms, feed-forward networks, normalization,
and residual connections.
""",

"""
SYSTEM: Correct factual mistakes politely.

USER: Training and inference are exactly the same process.

ASSISTANT: They are related but different. During training, model parameters
are updated using a loss and gradients. During inference, the trained
parameters are normally kept fixed while the model produces predictions.
"""
]


# ============================================================
# Build corpus
# ============================================================

datasets = {
    "knowledge.txt": knowledge,
    "conversations.txt": conversations,
    "instructions.txt": instructions,
    "coding.txt": coding,
    "reasoning.txt": reasoning,
    "corrections.txt": corrections,
}


for filename, examples in datasets.items():

    path = OUTPUT_DIR / filename

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        for example in examples:

            file.write(
                example.strip()
            )

            file.write(
                "\n\n"
            )

    print(
        f"Created {path}"
    )


# ============================================================
# Combined training corpus
# ============================================================

combined = []

for filename in datasets:

    path = OUTPUT_DIR / filename

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        combined.append(
            file.read()
        )


random.shuffle(combined)

training_file = OUTPUT_DIR / "train.txt"

with open(
    training_file,
    "w",
    encoding="utf-8"
) as file:

    for section in combined:

        file.write(
            section
        )

        file.write(
            "\n\n"
        )


print()
print(
    f"Created {training_file}"
)

print(
    "Dataset generation complete."
)