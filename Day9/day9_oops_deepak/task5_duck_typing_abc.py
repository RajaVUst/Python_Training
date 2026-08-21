from abc import ABC, abstractmethod

# (a) Duck-typed version — no shared base class
class Cleaner:
    def process(self, data):
        return data.strip()

class Tokenizer:
    def process(self, data):
        return data.split()

class Normalizer:
    def process(self, data):
        return [w.lower() for w in data]

def run_pipeline(steps, data):
    for step in steps:
        data = step.process(data)
    return data

# (b) ABC-enforced version — a real contract, like a Java interface
class Step(ABC):
    @abstractmethod
    def process(self, data):
        ...

class CleanerABC(Step):
    def process(self, data):
        return data.strip()

class TokenizerABC(Step):
    def process(self, data):
        return data.split()

class NormalizerABC(Step):
    def process(self, data):
        return [w.lower() for w in data]

def run_pipeline_abc(steps, data):
    for step in steps:
        data = step.process(data)
    return data

# (c) Duck typing suits small/internal code; ABC suits shared team code

print(run_pipeline([Cleaner(), Tokenizer(), Normalizer()], "  Hello WORLD  "))
print(run_pipeline_abc([CleanerABC(), TokenizerABC(), NormalizerABC()], "  Hello WORLD  "))

try:
    Step()
except TypeError as e:
    print(f"TypeError: {e}")

# Output:
# ['hello', 'world']
# ['hello', 'world']
# TypeError: Can't instantiate abstract class Step without an implementation for abstract method 'process'