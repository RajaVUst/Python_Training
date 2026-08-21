#Task 5 - Duck Typing vs Interfaces (ABCs)
#PART 1: DUCK TYPING APPROACH
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
text = "   Hello PYTHON World   "
result = run_pipeline(steps, text)
print(result)
 
#output
'''['hello', 'python', 'world']'''

 
#PART 2: ABSTRACT BASE CLASS (ABC) APPROACH
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
        return [word.lower() for word in data]
def run_pipeline(steps, data):
    for step in steps:
        data = step.process(data)
    return data
steps = [Cleaner(), Tokenizer(), Normalizer()]
text = "   Hello PYTHON World   "
result = run_pipeline(steps, text)
print(result)
print()
try:
    step = Step()
except TypeError as e:
    print("Error:")
    print(e)

 
#output
'''['hello', 'python', 'world']
 
Error:
Can't instantiate abstract class Step
with abstract method process'''
 
#note
'''Duck typing is useful when flexibility is needed and
any object with a process() method should work.
 
ABCs are useful in larger projects because they enforce
a contract and ensure required methods are implemented.'''