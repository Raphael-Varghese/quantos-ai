from pathlib import Path
import random


# ============================================================
# Paths
# ============================================================

OUTPUT_DIR = Path("data/raw")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# Dataset helpers
# ============================================================

def conversation(
    system,
    user,
    assistant
):

    return f"""<bos>
<system>
{system.strip()}

<user>
{user.strip()}

<assistant>
{assistant.strip()}

<end>
"""


DEFAULT_SYSTEM = (
    "You are Mosaic, a helpful general-purpose "
    "artificial intelligence assistant."
)


# ============================================================
# General knowledge
# ============================================================

knowledge = [

conversation(
    DEFAULT_SYSTEM,
    "What is artificial intelligence?",
    """
Artificial intelligence is the field of creating computer systems that
perform tasks that normally require capabilities associated with human
intelligence, such as recognizing patterns, processing language, making
predictions, and solving problems.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is machine learning?",
    """
Machine learning is a branch of artificial intelligence in which models
learn statistical patterns from data instead of being explicitly programmed
with every rule needed to perform a task.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is deep learning?",
    """
Deep learning is a type of machine learning based on neural networks with
multiple computational layers. These networks can learn increasingly complex
representations from data.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a language model?",
    """
A language model is a model that learns statistical relationships between
tokens or pieces of text. An autoregressive language model predicts the next
token based on the preceding context.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a Transformer?",
    """
A Transformer is a neural network architecture that uses attention
mechanisms to process relationships between elements in a sequence.
Transformers are widely used in modern language models.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is attention?",
    """
Attention allows a neural network to determine which parts of an input
sequence are more relevant when computing a representation for a particular
position.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a neural network?",
    """
A neural network is a computational model composed of layers that transform
input representations using learned parameters. During training, those
parameters are adjusted to reduce a loss function.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is overfitting?",
    """
Overfitting occurs when a model becomes too specialized to its training data
and performs poorly on new data. Comparing training and validation
performance can help identify overfitting.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a validation set?",
    """
A validation set is data that is kept separate from the examples used for
parameter updates. It provides an estimate of how well the model generalizes
to data that was not directly used for training.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is an optimizer?",
    """
An optimizer updates neural network parameters using information from
gradients. Adam and AdamW are examples of optimizers commonly used for
training neural networks.
"""
),

]


# ============================================================
# Python
# ============================================================

python_examples = [

conversation(
    DEFAULT_SYSTEM,
    "What is Python?",
    """
Python is a general-purpose programming language known for readable syntax
and a large ecosystem of libraries. It is commonly used for web development,
automation, scientific computing, data analysis, and artificial intelligence.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a Python variable?",
    """
A Python variable is a name that refers to an object. For example:

x = 10

Here, the name x refers to the integer object 10.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a Python list?",
    """
A Python list is an ordered, mutable collection. Lists can contain multiple
values and can be modified after they are created.

Example:

numbers = [1, 2, 3]
numbers.append(4)
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a Python dictionary?",
    """
A Python dictionary stores associations between keys and values.

Example:

person = {
    "name": "Alex",
    "age": 25
}

A value can be accessed using its key:

person["name"]
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a Python function?",
    """
A function is a reusable block of code that can accept inputs and produce
an output.

Example:

def add(a, b):
    return a + b
"""
),

conversation(
    DEFAULT_SYSTEM,
    "How do I handle an exception in Python?",
    """
Python uses try and except blocks to handle exceptions.

Example:

try:
    value = int(text)
except ValueError:
    print("Invalid number")
"""
),

conversation(
    DEFAULT_SYSTEM,
    "How do I read a text file in Python?",
    """
A text file can be opened using the with statement:

with open("file.txt", "r", encoding="utf-8") as file:
    text = file.read()

The with statement automatically closes the file when the block finishes.
"""
),

]


# ============================================================
# Programming
# ============================================================

programming = [

conversation(
    DEFAULT_SYSTEM,
    "Write a Python function that checks whether a number is even.",
    """
def is_even(number):
    return number % 2 == 0
"""
),

conversation(
    DEFAULT_SYSTEM,
    "Write a Python function that calculates the factorial of a number.",
    """
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1

    for value in range(2, n + 1):
        result *= value

    return result
"""
),

conversation(
    DEFAULT_SYSTEM,
    "Write a Python function that finds the largest number in a list.",
    """
def find_largest(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest
"""
),

conversation(
    DEFAULT_SYSTEM,
    "Write a Python function that reverses a string.",
    """
def reverse_string(text):
    return text[::-1]
"""
),

conversation(
    DEFAULT_SYSTEM,
    "How can I count the number of words in a string?",
    """
You can split the string on whitespace and count the resulting elements.

Example:

text = "hello world"
word_count = len(text.split())
"""
),

]


# ============================================================
# Mathematics
# ============================================================

mathematics = [

conversation(
    DEFAULT_SYSTEM,
    "What is 12 multiplied by 8?",
    """
12 × 8 = 96.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is 144 divided by 12?",
    """
144 ÷ 12 = 12.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "If a box contains 5 groups of 8 objects, how many objects are there?",
    """
There are 5 groups with 8 objects each.

5 × 8 = 40.

Therefore, there are 40 objects.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is the difference between a mean and a median?",
    """
The mean is calculated by adding the values and dividing by the number of
values. The median is the middle value after the data is sorted. The median
is generally less affected by extreme values than the mean.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is a prime number?",
    """
A prime number is an integer greater than 1 that has exactly two positive
divisors: 1 and itself. Examples include 2, 3, 5, 7, and 11.
"""
),

]


# ============================================================
# Reasoning
# ============================================================

reasoning = [

conversation(
    DEFAULT_SYSTEM,
    "Why might a larger model not always perform better?",
    """
A larger model has more representational capacity, but model size alone
does not guarantee better performance. Results also depend on data quality,
data quantity, architecture, optimization, regularization, and training
compute.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "Why is validation data useful?",
    """
Validation data provides a way to evaluate a model on examples that were not
used directly for parameter updates. It can reveal whether improvements on
the training data are also reflected in generalization.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "Why does a language model need a tokenizer?",
    """
Neural networks operate on numerical representations. A tokenizer converts
text into discrete tokens that can then be represented by integer IDs and
processed by the neural network.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "What is gradient clipping?",
    """
Gradient clipping limits the magnitude of gradients before an optimizer
updates model parameters. It can help prevent unstable updates caused by
very large gradients.
"""
),

]


# ============================================================
# Corrections
# ============================================================

corrections = [

conversation(
    DEFAULT_SYSTEM,
    "Python is exactly the same as C because both are compiled languages.",
    """
That statement is not accurate. Python and C have different language
designs and implementation models. Many Python implementations perform
compilation or bytecode generation internally, but Python is generally
described as a high-level language with multiple implementation strategies.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "A Transformer is not a neural network.",
    """
That statement is incorrect. A Transformer is a neural network architecture.
It uses components such as attention, feed-forward networks, normalization,
and residual connections.
"""
),

conversation(
    DEFAULT_SYSTEM,
    "Training and inference are exactly the same process.",
    """
Training and inference are related but different. During training, model
parameters are updated using gradients derived from a loss. During inference,
the trained parameters are normally kept fixed while the model generates
predictions.
"""
),

]


# ============================================================
# Combine
# ============================================================

datasets = {

    "knowledge": knowledge,

    "python": python_examples,

    "programming": programming,

    "mathematics": mathematics,

    "reasoning": reasoning,

    "corrections": corrections,

}


# ============================================================
# Write individual datasets
# ============================================================

for name, examples in datasets.items():

    path = (
        OUTPUT_DIR
        /
        f"{name}.txt"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        for example in examples:

            file.write(
                example
            )

            file.write(
                "\n"
            )

    print(
        f"Created {path}"
    )


# ============================================================
# Combined corpus
# ============================================================

combined = []

for name, examples in datasets.items():

    combined.extend(
        examples
    )


random.seed(1337)

random.shuffle(
    combined
)


training_file = (
    OUTPUT_DIR / "train.txt"
)


with open(
    training_file,
    "w",
    encoding="utf-8"
) as file:

    for example in combined:

        file.write(
            example
        )

        file.write(
            "\n"
        )


print()

print(
    f"Created {training_file}"
)

print(
    f"Total examples: "
    f"{len(combined)}"
)

print()

print(
    "Dataset generation complete."
)