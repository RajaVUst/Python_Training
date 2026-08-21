# Task 3 - Contrast Contracts
# Demonstrates duck typing vs abstract base classes (ABC)

from abc import ABC, abstractmethod


# ─── Part A: Duck Typing ───────────────────────────────────────────────────────
# No shared base class — any object with a .process() method will work.

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

result = run_pipeline([Cleaner(), Normalizer(), Tokenizer()], "  Hello World  ")
print("Duck-typed pipeline result:", result)


# ─── Part B: ABC Version ───────────────────────────────────────────────────────
# Enforces that every step MUST implement process() — like a Java interface.

class Step(ABC):
    @abstractmethod
    def process(self, data): ...

class ABCCleaner(Step):
    def process(self, data):
        return data.strip()

class ABCTokenizer(Step):
    def process(self, data):
        return data.split()

class ABCNormalizer(Step):
    def process(self, data):
        return data.lower()

def run_abc_pipeline(steps, data):
    for step in steps:
        data = step.process(data)
    return data

result2 = run_abc_pipeline([ABCCleaner(), ABCNormalizer(), ABCTokenizer()], "  Hello World  ")
print("ABC pipeline result:", result2)

# Trying to instantiate Step directly raises TypeError
try:
    Step()
except TypeError as e:
    print("Cannot instantiate Step():", e)


# ─── Part C: When to use which? ───────────────────────────────────────────────
# Duck typing is fine for small, internal pipelines where you control all the code.
# Use ABC when building a shared library or framework where other developers must
# implement a specific interface — it gives an early, clear error if they forget a method.
