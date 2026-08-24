# DUNER METHODS

class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

    def __str__(self):
        return f"TrainingRun(model='{self.model_name}', lr={self.learning_rate})"

    def __eq__(self, other):
        return (
            self.model_name == other.model_name
            and self.learning_rate == other.learning_rate
        )

    def __repr__(self):
        return f"TrainingRun('{self.model_name}', {self.learning_rate})"


run1 = TrainingRun("GPT", 0.01)
run2 = TrainingRun("GPT", 0.01)
run3 = TrainingRun("BERT", 0.01)

print(run1)
print(run1 == run2)
print(run1 == run3)
print(repr(run1))

# Output:
# TrainingRun(model='GPT', lr=0.01)
# True
# False
# TrainingRun('GPT', 0.01)