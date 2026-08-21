class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

    def __str__(self):
        return f"TrainingRun(model='{self.model_name}', lr={self.learning_rate})"

    def __repr__(self):
        return f"TrainingRun(model_name={self.model_name!r}, learning_rate={self.learning_rate!r})"

    def __eq__(self, other):
        if not isinstance(other, TrainingRun):
            return NotImplemented
        return (self.model_name, self.learning_rate) == (other.model_name, other.learning_rate)


r1 = TrainingRun("gpt-mini", 0.01)
r2 = TrainingRun("gpt-mini", 0.01)

print(r1)
print(r1 == r2)

# Output:
# TrainingRun(model='gpt-mini', lr=0.01)
# True