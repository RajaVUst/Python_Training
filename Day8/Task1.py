class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        if not self.validate_learning_rate(learning_rate):
            raise ValueError("Learning rate must be between 0 and 1.")

        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "pending"

        TrainingRun.run_count += 1

    def start(self):
        self.status = "running"
        print(f"{self.model_name} training started.")

    def summary(self):
        return (
            f"Model: {self.model_name}, "
            f"Learning rate: {self.learning_rate}, "
            f"Status: {self.status}"
        )

    @classmethod
    def from_config(cls, config):
        return cls(
            config["model_name"],
            config["learning_rate"]
        )

    @staticmethod
    def validate_learning_rate(learning_rate):
        return 0 < learning_rate < 1


run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("bert-small", 0.001)

config = {
    "model_name": "resnet",
    "learning_rate": 0.05
}

run3 = TrainingRun.from_config(config)

run1.start()

print(run1.summary())
print(run2.summary())
print(run3.summary())

print("Total runs:", TrainingRun.run_count)

#output
'''
gpt-mini training started.
Model: gpt-mini, Learning rate: 0.01, Status: running
Model: bert-small, Learning rate: 0.001, Status: pending
Model: resnet, Learning rate: 0.05, Status: pending
Total runs: 3
'''