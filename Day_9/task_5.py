# 1) Duck-typed version
class Cleaner:
    def process(self, data):
        return data.strip()


class Tokenizer:
    def process(self, data):
        return data.split()


class Normalizer:
    def process(self, data):
        return [token.lower() for token in data]


def run_pipeline(steps, data):
    """Works with any object that provides .process(data)."""
    for step in steps:
        data = step.process(data)
    return data

duck_steps = [Cleaner(), Tokenizer(), Normalizer()]
result = run_pipeline(duck_steps, "  Hello WORLD Python  ")
print("Duck typing result:", result)


# 2) ABC (Abstract Base Class) version

from abc import ABC, abstractmethod


class Step(ABC):
    @abstractmethod
    def process(self, data):
        """Transform and return data."""
        pass


class CleanerStep(Step):
    def process(self, data):
        return data.strip()


class TokenizerStep(Step):
    def process(self, data):
        return data.split()


class NormalizerStep(Step):
    def process(self, data):
        return [token.lower() for token in data]


def run_pipeline_abc(steps, data):
    """Works with Step subclasses."""
    for step in steps:
        data = step.process(data)
    return data

abc_steps = [CleanerStep(), TokenizerStep(), NormalizerStep()]
result = run_pipeline_abc(abc_steps, "  Hello WORLD Python  ")
print("ABC result:", result)
try:
    Step()
except TypeError as e:
    print("Cannot instantiate Step:", e) 
    
# Duck typing is great when you want flexibility and don't need
# a formal inheritance hierarchy. Any object with a compatible
# process() method can participate in the pipeline.
#
# An ABC is useful on larger teams or frameworks where you want
# an explicit contract. It makes requirements self-documenting
# and catches missing method implementations at instantiation time.