class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"

        TrainingRun.run_count += 1

    def start(self):
        self._status = "running"

    def summary(self):
        return (
            f"Model: {self.model_name}, "
            f"Learning rate: {self.learning_rate}, "
            f"Status: {self._status}"
        )

    def __str__(self):
        return (
            f"TrainingRun("
            f"model='{self.model_name}', "
            f"lr={self.learning_rate}"
            f")"
        )

    def __repr__(self):
        return (
            f"TrainingRun("
            f"model_name='{self.model_name}', "
            f"learning_rate={self.learning_rate}"
            f")"
        )

    def __eq__(self, other):
        if not isinstance(other, TrainingRun):
            return NotImplemented

        return (
            self.model_name == other.model_name
            and self.learning_rate == other.learning_rate
        )


run1 = TrainingRun(
    "gpt-mini",
    0.01
)

run2 = TrainingRun(
    "gpt-mini",
    0.01
)

run3 = TrainingRun(
    "bert-small",
    0.001
)

print(run1)

print("run1 == run2:", run1 == run2)
print("run1 == run3:", run1 == run3)

print("Developer representation:", repr(run1))

# __str__ provides a readable representation for users.
# __repr__ provides a detailed representation mainly for developers and debugging.

#output
'''
TrainingRun(model='gpt-mini', lr=0.01)
run1 == run2: True
run1 == run3: False
Developer representation: TrainingRun(model_name='gpt-mini', learning_rate=0.01)

'''