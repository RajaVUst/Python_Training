from abc import ABC, abstractmethod


# Duck Typing Version

class Cleaner:
    def process(self, data):
        return data.strip()


class Tokenizer:
    def process(self, data):
        return data.split()


class Normalizer:
    def process(self, data):
        return [word.lower() for word in data]


def run_pipeline(steps, data):
    for step in steps:
        data = step.process(data)
    return data


steps = [Cleaner(), Tokenizer(), Normalizer()]
result = run_pipeline(steps, "   HELLO WORLD PYTHON   ")

print("Duck Typing Output:")
print(result)


# ABC (Interface-like) Version

class Step(ABC):

    @abstractmethod
    def process(self, data):
        pass


class CleanerStep(Step):
    def process(self, data):
        return data.strip()


class TokenizerStep(Step):
    def process(self, data):
        return data.split()


class NormalizerStep(Step):
    def process(self, data):
        return [word.lower() for word in data]


def run_pipeline_abc(steps, data):
    for step in steps:
        data = step.process(data)
    return data


steps_abc = [
    CleanerStep(),
    TokenizerStep(),
    NormalizerStep()
]

result_abc = run_pipeline_abc(
    steps_abc,
    "   HELLO WORLD PYTHON   "
)

print("\nABC Output:")
print(result_abc)


try:
    step = Step()
except TypeError as e:
    print("\nTypeError:", e)

# Output:
"""
Duck Typing Output:
['hello', 'world', 'python']

ABC Output:
['hello', 'world', 'python']
"""


"""
Duck typing is useful when you want flexibility and don't need to
enforce a strict contract. Any object with a process() method will work.

An ABC is useful on larger teams or projects where you want to enforce
that every pipeline step implements process(), making the code easier
to maintain and validate.
"""