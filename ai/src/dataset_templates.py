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
        example(
        "What is a Python string?",
        """
A string is a sequence of characters represented by the str type.

For example:

name = "Mosaic"

Strings can be indexed and sliced:

first = name[0]
part = name[0:3]
"""
    ),

    example(
        "What is a Python integer?",
        """
An integer is a whole-number value represented by the int type.

Examples include:

x = 10
y = -5
z = 0

Python integers can represent arbitrarily large whole numbers subject to
available memory.
"""
    ),

    example(
        "What is a Boolean in Python?",
        """
A Boolean represents a true or false value.

Python uses the bool type with the values True and False.

For example:

is_ready = True
is_finished = False

Boolean expressions are commonly used in conditions.
"""
    ),

    example(
        "How does an if statement work in Python?",
        """
An if statement runs a block of code when a condition is true.

For example:

if age >= 18:
    print("Adult")
else:
    print("Minor")

Python uses indentation to define the blocks controlled by the condition.
"""
    ),

    example(
        "What is a list comprehension?",
        """
A list comprehension is a compact way to construct a list from an iterable.

For example:

squares = [x * x for x in range(5)]

This creates a list containing the squares of the values from 0 through 4.
"""
    ),

    example(
        "What is the difference between a list and a tuple?",
        """
Both lists and tuples are ordered collections.

Lists are mutable, so their contents can be changed after creation.

Tuples are generally immutable after creation.

For example:

numbers = [1, 2, 3]
point = (10, 20)
"""
    ),

    example(
        "How do you define a class in Python?",
        """
A class defines a type that can combine data and behavior.

For example:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

An object can then be created from the class.
"""
    ),

    example(
        "What is a Python module?",
        """
A module is a Python file containing code such as functions, classes, and
variables.

For example, if math_utils.py contains a function called add, another file
can import it:

from math_utils import add

Modules help organize code into reusable components.
"""
    ),

    example(
        "What is a Python dictionary comprehension?",
        """
A dictionary comprehension creates a dictionary from an iterable.

For example:

squares = {x: x * x for x in range(5)}

The resulting dictionary maps each number to its square.
"""
    ),

    example(
        "What does enumerate do in Python?",
        """
enumerate returns an iterable that provides both an index and an item.

For example:

for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

This is useful when a loop needs both the position and the value.
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
        example(
        "What is a Python string?",
        """
A string is a sequence of characters represented by the str type.

For example:

name = "Mosaic"

Strings can be indexed and sliced:

first = name[0]
part = name[0:3]
"""
    ),

    example(
        "What is a Python integer?",
        """
An integer is a whole-number value represented by the int type.

Examples include:

x = 10
y = -5
z = 0

Python integers can represent arbitrarily large whole numbers subject to
available memory.
"""
    ),

    example(
        "What is a Boolean in Python?",
        """
A Boolean represents a true or false value.

Python uses the bool type with the values True and False.

For example:

is_ready = True
is_finished = False

Boolean expressions are commonly used in conditions.
"""
    ),

    example(
        "How does an if statement work in Python?",
        """
An if statement runs a block of code when a condition is true.

For example:

if age >= 18:
    print("Adult")
else:
    print("Minor")

Python uses indentation to define the blocks controlled by the condition.
"""
    ),

    example(
        "What is a list comprehension?",
        """
A list comprehension is a compact way to construct a list from an iterable.

For example:

squares = [x * x for x in range(5)]

This creates a list containing the squares of the values from 0 through 4.
"""
    ),

    example(
        "What is the difference between a list and a tuple?",
        """
Both lists and tuples are ordered collections.

Lists are mutable, so their contents can be changed after creation.

Tuples are generally immutable after creation.

For example:

numbers = [1, 2, 3]
point = (10, 20)
"""
    ),

    example(
        "How do you define a class in Python?",
        """
A class defines a type that can combine data and behavior.

For example:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

An object can then be created from the class.
"""
    ),

    example(
        "What is a Python module?",
        """
A module is a Python file containing code such as functions, classes, and
variables.

For example, if math_utils.py contains a function called add, another file
can import it:

from math_utils import add

Modules help organize code into reusable components.
"""
    ),

    example(
        "What is a Python dictionary comprehension?",
        """
A dictionary comprehension creates a dictionary from an iterable.

For example:

squares = {x: x * x for x in range(5)}

The resulting dictionary maps each number to its square.
"""
    ),

    example(
        "What does enumerate do in Python?",
        """
enumerate returns an iterable that provides both an index and an item.

For example:

for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

This is useful when a loop needs both the position and the value.
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
        example(
        "What is 15 percent of 80?",
        """
15 percent is 0.15.

0.15 × 80 = 12.

Therefore, 15 percent of 80 is 12.
"""
    ),

    example(
        "What is the area of a rectangle with length 8 and width 5?",
        """
The area of a rectangle is:

area = length × width

8 × 5 = 40.

Therefore, the area is 40 square units.
"""
    ),

    example(
        "What is the perimeter of a rectangle with length 8 and width 5?",
        """
The perimeter of a rectangle is:

2 × (length + width)

2 × (8 + 5) = 26.

Therefore, the perimeter is 26 units.
"""
    ),

    example(
        "Solve x + 7 = 12.",
        """
Subtract 7 from both sides:

x + 7 - 7 = 12 - 7

x = 5.

Therefore, x is 5.
"""
    ),

    example(
        "Solve 3x = 21.",
        """
Divide both sides by 3:

3x / 3 = 21 / 3

x = 7.

Therefore, x is 7.
"""
    ),

    example(
        "What is the probability of getting heads when flipping a fair coin?",
        """
A fair coin has two equally likely outcomes: heads and tails.

The probability of heads is:

1 / 2 = 0.5

Therefore, the probability is 1/2, or 50 percent.
"""
    ),

    example(
        "What is the median of 2, 4, 7, 9, and 12?",
        """
The values are already ordered.

There are five values, so the middle value is the third value.

The median is 7.
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
        example(
        "What is 15 percent of 80?",
        """
15 percent is 0.15.

0.15 × 80 = 12.

Therefore, 15 percent of 80 is 12.
"""
    ),

    example(
        "What is the area of a rectangle with length 8 and width 5?",
        """
The area of a rectangle is:

area = length × width

8 × 5 = 40.

Therefore, the area is 40 square units.
"""
    ),

    example(
        "What is the perimeter of a rectangle with length 8 and width 5?",
        """
The perimeter of a rectangle is:

2 × (length + width)

2 × (8 + 5) = 26.

Therefore, the perimeter is 26 units.
"""
    ),

    example(
        "Solve x + 7 = 12.",
        """
Subtract 7 from both sides:

x + 7 - 7 = 12 - 7

x = 5.

Therefore, x is 5.
"""
    ),

    example(
        "Solve 3x = 21.",
        """
Divide both sides by 3:

3x / 3 = 21 / 3

x = 7.

Therefore, x is 7.
"""
    ),

    example(
        "What is the probability of getting heads when flipping a fair coin?",
        """
A fair coin has two equally likely outcomes: heads and tails.

The probability of heads is:

1 / 2 = 0.5

Therefore, the probability is 1/2, or 50 percent.
"""
    ),

    example(
        "What is the median of 2, 4, 7, 9, and 12?",
        """
The values are already ordered.

There are five values, so the middle value is the third value.

The median is 7.
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
        example(
        "If a train travels 60 kilometers in 2 hours at a constant speed, how far will it travel in 5 hours?",
        """
The train travels 60 kilometers in 2 hours.

Its speed is:

60 ÷ 2 = 30 kilometers per hour.

In 5 hours it will travel:

30 × 5 = 150 kilometers.

Therefore, it will travel 150 kilometers.
"""
    ),

    example(
        "A number is increased from 50 to 65. What is the percentage increase?",
        """
The increase is:

65 - 50 = 15.

Divide the increase by the original value:

15 / 50 = 0.3.

Convert to a percentage:

0.3 × 100 = 30 percent.

Therefore, the percentage increase is 30 percent.
"""
    ),

    example(
        "Why can a program produce different results when randomness is involved?",
        """
A program may produce different results when it uses random choices.

If the random generator is not given a fixed seed, different executions can
produce different random sequences.

A fixed seed can make many pseudorandom processes reproducible.
"""
    ),

    example(
        "What should you do when a programming problem has multiple possible interpretations?",
        """
First identify the ambiguity and determine whether it changes the result.

If the intended interpretation is clear from the context, state the
assumption and proceed.

If the ambiguity materially affects the answer and cannot be resolved from
the available information, ask a concise clarification question.
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
        example(
        "Why does this Python code fail? numbers = [1, 2, 3]; print(numbers[3])",
        """
The list contains three elements, whose valid indexes are 0, 1, and 2.

Index 3 is outside the valid range, so Python raises an IndexError.

Use a valid index or check the length of the list before accessing an
element.
"""
    ),

    example(
        "Why does this Python code fail? print(name) when name was never defined.",
        """
Python raises a NameError because the name variable does not exist in the
current scope.

Define the variable before using it, or correct the variable name if a
different variable was intended.
"""
    ),

    example(
        "Why does this code produce a TypeError? 5 + '3'",
        """
The expression attempts to add an integer and a string.

Python does not automatically combine these two different types with the +
operator.

Convert the values to compatible types depending on the intended operation.
"""
    ),

    example(
        "Why does this Python function produce the wrong result? def add(a, b): print(a + b)",
        """
The function prints the result but does not return it.

If the caller expects a value, the function should use return:

def add(a, b):
    return a + b

Then the result can be stored or used by the calling code.
"""
    ),

    example(
        "What is a good first step when debugging an unfamiliar error?",
        """
Start by reading the error message and traceback carefully.

Identify the exception type, the line where it occurred, and the values or
assumptions involved.

Then reduce the problem to the smallest reproducible example you can create.
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
        example(
        "Python lists cannot be changed after they are created.",
        """
That is incorrect. Python lists are mutable.

For example:

numbers = [1, 2, 3]
numbers.append(4)

The list now contains four elements.
"""
    ),

    example(
        "A Python tuple is always completely immutable in every sense.",
        """
A tuple itself is immutable, meaning its elements cannot be replaced through
normal tuple assignment.

However, a tuple can contain mutable objects such as lists, and those objects
may still be modified.
"""
    ),

    example(
        "A validation set is used to update model weights directly.",
        """
Normally, validation data is used to evaluate the model rather than directly
update its parameters.

Training data is used for parameter updates. Validation results can help
monitor generalization and guide training decisions.
"""
    ),

    example(
        "More training always makes a neural network better.",
        """
Not necessarily. Training for too long on limited data can lead to
overfitting.

Model performance depends on factors including the data, architecture,
optimization, regularization, and training duration.
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
        example(
        "Explain a variable simply.",
        """
A variable is a name that refers to a value or object.

For example:

age = 13

Here, age is the variable name and 13 is the value it refers to.
"""
    ),

    example(
        "Explain a loop simply.",
        """
A loop repeats a block of code.

For example, a for loop can process every item in a list:

for item in items:
    print(item)

Loops are useful when the same operation needs to be performed multiple
times.
"""
    ),

    example(
        "Explain an exception simply.",
        """
An exception is an event that indicates something went wrong while a program
was running.

Python can handle exceptions with constructs such as try and except.
"""
    ),

    example(
        "Explain training versus inference simply.",
        """
Training is when a model's parameters are adjusted using examples and a
loss.

Inference is when the trained model is used to produce outputs for new
inputs without normally changing its parameters.
"""
    ),

    example(
        "Explain a tokenizer simply.",
        """
A tokenizer converts text into smaller units called tokens.

A language model can then convert those tokens into numerical IDs and process
them with a neural network.
"""
    ),

    example(
        "Explain attention simply.",
        """
Attention allows a model to determine which parts of the available context
are important when computing a representation.

In a language model, attention helps tokens use information from relevant
other tokens in the context.
"""
    ),

]