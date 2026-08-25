from abc import ABC,abstractmethod

class Step(ABC):
    
    @abstractmethod
    def process(self,data):
        pass
    
class Cleaner(Step):
    def process(self,data):
        return data.strip()
    
class Tokenizer(Step):
    def process(self, data):
        return data.split()
    
class Normalizer(Step):
    def process(self, data):
        return [word.lower() for word in data]
    
    
def run_pipeline(steps,data):
    for step in steps:
        data=step.process(data)
        
    return data

steps=[Cleaner(),
       Tokenizer(),
       Normalizer()]

result=run_pipeline(steps,"  HELLO WORLD   ")

print(result)

# OUTPUT

# ['hello', 'world']
