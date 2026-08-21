#Task 6 - Dunder Methods

class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
    def __str__(self):
        return (
            f"TrainingRun(model='{self.model_name}', "
            f"lr={self.learning_rate})"
        )
    def __eq__(self, other):
        if not isinstance(other, TrainingRun):
            return False
        return (
            self.model_name == other.model_name and
            self.learning_rate == other.learning_rate
        )
    def __repr__(self):
        return (
            f"TrainingRun(model_name='{self.model_name}', "
            f"learning_rate={self.learning_rate})"
        )
run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("gpt-mini", 0.01)
run3 = TrainingRun("gpt-large", 0.001)
print("Run 1:")
print(run1)
print()
print("run1 == run2:", run1 == run2)
print("run1 == run3:", run1 == run3)
print()
print("repr(run1):")
print(repr(run1))

 
#output
'''Run 1:
TrainingRun(model='gpt-mini', lr=0.01)
 
run1 == run2: True
run1 == run3: False
 
repr(run1):
TrainingRun(model_name='gpt-mini', learning_rate=0.01)'''

 
#note
'''__str__ is intended for end users and provides a clean,
human-readable description of an object.
 
__repr__ is intended for developers and provides a more
detailed representation that is useful for debugging.'''