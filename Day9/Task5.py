#Duck Typing

class Cleaner:

    def process(self, data):
        return data.strip()


class Tokenizer:

    def process(self, data):
        return data.split()


class Normalizer:

    def process(self, data):
        return data.lower()


def run_pipeline(steps, data):

    for step in steps:
        data = step.process(data)

    return data


steps = [
    Cleaner(),
    Tokenizer()
]

result = run_pipeline(
    steps,
    "  HELLO PYTHON  "
)

print(result)


# OUTPUT:
# ['HELLO', 'PYTHON']

# Abstract Base Class
from abc import ABC, abstractmethod

class Step(ABC):

    @abstractmethod
    def process(self, data):
        pass

class Cleaner(Step):

    def process(self, data):
        return data.strip()


class Tokenizer(Step):

    def process(self, data):
        return data.split()


class Normalizer(Step):

    def process(self, data):
        return data.lower()


def run_pipeline(steps, data):

    for step in steps:
        data = step.process(data)

    return data

steps = [
    Cleaner(),
    Normalizer()
]

result = run_pipeline(
    steps,
    "  HELLO PYTHON  "
)

print(result)


try:
    step = Step()
except TypeError as e:
    print("Error:", e)


# OUTPUT:
# hello python
# Error: Can't instantiate abstract class Step without an implementation for abstract method 'process'

# Duck typing:
# Use duck typing when the team wants flexibility and the required behavior
# is simple and well understood.

# ABC:
# Use an Abstract Base Class when the team needs an explicit contract
# and wants subclasses to implement required methods.