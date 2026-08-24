# Contrast duck typing / ABCs with Java's interfaces

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
    Normalizer(),
    Tokenizer()
]
result = run_pipeline(steps, "  HELLO PYTHON  ")
print(result)

# Output:
# ['hello', 'python']


# PART2- ABC
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
    Normalizer(),
    Tokenizer()
]

result = run_pipeline(steps, "  HELLO PYTHON  ")
print(result)
# Test the abstract class
step = Step()

# Output:
# ['hello', 'python']
# Type Error