class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        TrainingRun.run_count += 1

    def training_start(self):
        print(f"{self.model_name} training started")

    def training_summary(self):
        return {
            "Model Name": self.model_name,
            "Learning Rate": self.learning_rate
        }

    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )

    def __str__(self):
        return (
            f"TrainingRun(model='{self.model_name}', "
            f"lr={self.learning_rate})"
        )

    def __eq__(self, other):
        if not isinstance(other, TrainingRun):
            return False

        return (
            self.model_name == other.model_name
            and self.learning_rate == other.learning_rate
        )


run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("gpt-mini", 0.01)
run3 = TrainingRun("bert", 0.001)

print(run1)

print(run1 == run2)
print(run1 == run3)

print("Total runs:", TrainingRun.run_count)

# Output:
"""TrainingRun(model='gpt-mini', lr=0.01)
True
False
Total runs: 3"""