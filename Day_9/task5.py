# DUCK TYPING & INTERFACES

from abc import ABC, abstractmethod

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


steps = [
    Cleaner(),
    Tokenizer(),
    Normalizer()
]

print(run_pipeline(steps, " HELLO WORLD PYTHON "))


class Step(ABC):
    @abstractmethod
    def process(self, data):
        pass


class CleanerABC(Step):
    def process(self, data):
        return data.strip()


class TokenizerABC(Step):
    def process(self, data):
        return data.split()


class NormalizerABC(Step):
    def process(self, data):
        return [word.lower() for word in data]


steps_abc = [
    CleanerABC(),
    TokenizerABC(),
    NormalizerABC()
]

print(run_pipeline(steps_abc, " HELLO WORLD PYTHON "))

try:
    step = Step()
except TypeError as e:
    print(e)

# Output:
# ['hello', 'world', 'python']
# ['hello', 'world', 'python']
# Can't instantiate abstract class Step with abstract method process