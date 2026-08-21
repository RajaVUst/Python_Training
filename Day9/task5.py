class Cleaner:
    def process(self,data):
        return data.strip()
class Tokenizer:
    def process(self,data):
        return data.split()
class Normalizer:
    def process(self,data):
        return [len(word) for word in data]

def run_pipeline(steps,data):
    for step in steps:
        data = step.process(data)
    return data

steps = [Cleaner(),Tokenizer(),Normalizer()]
print(run_pipeline(steps,"  This is Day9 Python Programming Tasks"))
# Output -> [4, 2, 4, 6, 11, 5]

#with ABC
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
        return [len(word) for word in data]
def run_pipeline(steps, data):
    for step in steps:
        data = step.process(data)
    return data
steps = [Cleaner(), Tokenizer(), Normalizer()]
text = "   Welcome to PYTHON World   "
result = run_pipeline(steps, text)
print(result)      # [7, 2, 6, 5]
print()
try:
    step = Step()   # Can't instantiate abstract class Step without an implementation for abstract method 'process'
except TypeError as e:
    print("Error:")
    print(e)