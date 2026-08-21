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
print(run1)     # TrainingRun(model='gpt-mini', lr=0.01)
print("run1 == run2:", run1 == run2)    # True
print("run1 == run3:", run1 == run3)    # False
print(repr(run1))   # TrainingRun(model_name='gpt-mini', learning_rate=0.01)