class Cleaner:
    def process(self,data):
        return data.strip()

class Tokenizer:
    def process(self,data):
        return data.split()
    
class Normalizer:
    def process(self,data):
        return[word.lower() for word in data]

def run_pipeline(steps,data):
    for step in steps:
        data=step.process(data)
        
    return data

steps=[Cleaner(),
       Tokenizer(),
       Normalizer()]

result=run_pipeline(steps,"  HELLO WORLD   ")

print(result)        
