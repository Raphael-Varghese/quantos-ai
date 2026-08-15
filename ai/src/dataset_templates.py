# ============================================================
# Mosaic Dataset Templates
# ============================================================

SYSTEM = (
    "You are Mosaic, a helpful general-purpose "
    "artificial intelligence assistant."
)


def example(user, assistant, system=SYSTEM):

    return f"""<bos>
<system>
{system}

<user>
{user}

<assistant>
{assistant}

<end>
"""


# ============================================================
# Python
# ============================================================

PYTHON_EXAMPLES = [

    example(
        "What is a Python variable?",
        """
A Python variable is a name that refers to an object.

For example:

x = 10

Here, x refers to the integer value 10.
"""
    ),

    example(
        "What is a Python list?",
        """
A Python list is an ordered, mutable collection.

For example:

numbers = [1, 2, 3]

You can modify a list after creating it:

numbers.append(4)
"""
    ),

    example(
        "What is a Python tuple?",
        """
A tuple is an ordered collection that is generally immutable after it is
created.

For example:

point = (10, 20)

Tuples are useful for representing fixed collections of values.
"""
    ),

    example(
        "What is a Python dictionary?",
        """
A dictionary stores key-value associations.

For example:

person = {
    "name": "Alex",
    "age": 25
}

You can access a value using its key:

person["name"]
"""
    ),

    example(
        "What is a Python set?",
        """
A set is a collection of unique elements.

For example:

numbers = {1, 2, 3, 3}

The resulting set contains only one copy of each value.
"""
    ),

    example(
        "What is a Python function?",
        """
A function is a reusable block of code.

For example:

def add(a, b):
    return a + b

The function accepts two arguments and returns their sum.
"""
    ),

    example(
        "How do you write a loop in Python?",
        """
A for loop can iterate over the elements of a sequence.

Example:

for number in numbers:
    print(number)

Python also provides while loops for repeating code while a condition
remains true.
"""
    ),

    example(
        "How do you handle errors in Python?",
        """
Python uses try and except blocks to handle exceptions.

Example:

try:
    value = int(text)
except ValueError:
    print("Invalid number")
"""
    ),

    example(
        "How do you read a file in Python?",
        """
The with statement can be used to safely open a file.

Example:

with open("file.txt", "r", encoding="utf-8") as file:
    text = file.read()

The file is automatically closed when the with block finishes.
"""
    ),

]


# ============================================================
# Programming
# ============================================================

PROGRAMMING_EXAMPLES = [

    example(
        "Write a Python function that adds two numbers.",
        """
def add(a, b):
    return a + b
"""
    ),

    example(
        "Write a Python function that checks whether a number is even.",
        """
def is_even(number):
    return number % 2 == 0
"""
    ),

    example(
        "Write a Python function that squares a number.",
        """
def square(number):
    return number * number
"""
    ),

    example(
        "Write a Python function that finds the largest value in a list.",
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

    example(
        "Write a Python function that reverses a string.",
        """
def reverse_string(text):
    return text[::-1]
"""
    ),

    example(
        "Write a Python function that counts the words in a string.",
        """
def count_words(text):
    return len(text.split())
"""
    ),

    example(
        "Write a Python function that calculates a factorial.",
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

]


# ============================================================
# Mathematics
# ============================================================

MATH_EXAMPLES = [

    example(
        "What is 5 times 8?",
        """
5 × 8 = 40.

Therefore, the answer is 40.
"""
    ),

    example(
        "What is 144 divided by 12?",
        """
144 ÷ 12 = 12.

Therefore, the answer is 12.
"""
    ),

    example(
        "What is 25 percent of 200?",
        """
25 percent is 0.25.

0.25 × 200 = 50.

Therefore, 25 percent of 200 is 50.
"""
    ),

    example(
        "What is a prime number?",
        """
A prime number is an integer greater than 1 that has exactly two positive
divisors: 1 and itself.

Examples include 2, 3, 5, 7, and 11.
"""
    ),

    example(
        "What is the mean of 2, 4, 6, and 8?",
        """
Add the values:

2 + 4 + 6 + 8 = 20

There are four values:

20 ÷ 4 = 5

Therefore, the mean is 5.
"""
    ),

]


# ============================================================
# AI / ML
# ============================================================

AI_EXAMPLES = [

    example(
        "What is machine learning?",
        """
Machine learning is a branch of artificial intelligence in which models
learn patterns from data rather than being explicitly programmed with every
rule needed to perform a task.
"""
    ),

    example(
        "What is deep learning?",
        """
Deep learning is a type of machine learning based on neural networks with
multiple computational layers.
"""
    ),

    example(
        "What is a neural network?",
        """
A neural network is a mathematical model composed of layers of learned
parameters that transform input representations.
"""
    ),

    example(
        "What is a Transformer?",
        """
A Transformer is a neural network architecture that uses attention
mechanisms to process relationships between elements in a sequence.
"""
    ),

    example(
        "What is self-attention?",
        """
Self-attention allows each position in a sequence to use information from
other positions when computing its representation.
"""
    ),

    example(
        "What is a language model?",
        """
A language model learns statistical relationships between tokens and can
assign probabilities to possible sequences. An autoregressive language model
can generate text by predicting one token at a time.
"""
    ),

    example(
        "What is gradient descent?",
        """
Gradient descent is an optimization method that updates parameters in a
direction intended to reduce the value of a loss function.
"""
    ),

    example(
        "What is overfitting?",
        """
Overfitting occurs when a model learns the training data too specifically
and performs worse on examples it has not seen during training.
"""
    ),

]


# ============================================================
# Reasoning
# ============================================================

REASONING_EXAMPLES = [

    example(
        "A box contains 6 groups of 7 objects. How many objects are there?",
        """
There are 6 groups and each group contains 7 objects.

6 × 7 = 42.

Therefore, there are 42 objects.
"""
    ),

    example(
        "A program processes 50 records in 5 seconds. How many records can it process in 20 seconds at the same rate?",
        """
20 seconds is four times 5 seconds.

50 × 4 = 200.

Therefore, the program can process approximately 200 records in 20 seconds
under the stated constant-rate assumption.
"""
    ),

    example(
        "Why might a larger neural network perform worse than a smaller one?",
        """
Model size is only one factor affecting performance. Data quality,
optimization, regularization, architecture, and training procedure also
matter. A larger model can perform poorly if it is trained inadequately or
does not generalize well.
"""
    ),

]


# ============================================================
# Debugging
# ============================================================

DEBUGGING_EXAMPLES = [

    example(
        "Why does this Python code fail? x = 10 / 0",
        """
The expression attempts to divide by zero. Python raises a ZeroDivisionError
because division by zero is undefined.

You can prevent the exception by checking the denominator before performing
the division or by handling the exception appropriately.
"""
    ),

    example(
        "Why does Python raise an IndexError when accessing list[10]?",
        """
An IndexError occurs when you try to access a list position that does not
exist. If a list contains fewer than 11 elements, index 10 is outside the
valid range.
"""
    ),

    example(
        "Why does a Python function return None when I expected a value?",
        """
A function returns None when it reaches the end without executing a return
statement with a value.

For example:

def add(a, b):
    result = a + b

The function calculates the result but never returns it.
"""
    ),

]


# ============================================================
# Corrections
# ============================================================

CORRECTION_EXAMPLES = [

    example(
        "Python is exactly the same as C.",
        """
Python and C are different programming languages with different designs,
syntax, type systems, and typical implementation strategies.
"""
    ),

    example(
        "A Transformer is not a neural network.",
        """
That is incorrect. A Transformer is a neural network architecture built from
components including attention, feed-forward networks, normalization, and
residual connections.
"""
    ),

    example(
        "Inference updates the model weights every time.",
        """
Normally, inference does not update the model's learned parameters. During
inference the trained weights are used to produce predictions.
"""
    ),

]


# ============================================================
# Explanations
# ============================================================

EXPLANATION_EXAMPLES = [

    example(
        "Explain recursion simply.",
        """
Recursion is a programming technique in which a function calls itself on a
smaller version of a problem. A recursive function needs a base case that
stops the recursion.
"""
    ),

    example(
        "Explain an API simply.",
        """
An API is an interface that allows different software components to
communicate using defined operations and data formats.
"""
    ),

    example(
        "Explain a database simply.",
        """
A database is a system for storing and organizing data so that applications
can efficiently create, retrieve, update, and manage that data.
"""
    ),

]