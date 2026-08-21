class TrainingRun:

    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "Not Started"

        TrainingRun.run_count += 1

    def start(self):
        self.status = "Running"
        print(f"{self.model_name} training started.")

    def summary(self):
        print(f"Model: {self.model_name}")
        print(f"Learning Rate: {self.learning_rate}")
        print(f"Status: {self.status}")

    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )

    @staticmethod
    def validate_learning_rate(learning_rate):
        return 0 < learning_rate < 1


run1 = TrainingRun("Model-A", 0.01)
run2 = TrainingRun("Model-B", 0.001)
run3 = TrainingRun("Model-C", 0.05)

print("Run count:", TrainingRun.run_count)

run1.start()
run1.summary()

config = {
    "model_name": "Model-D",
    "learning_rate": 0.02
}

run4 = TrainingRun.from_config(config)
run4.summary()

print(TrainingRun.validate_learning_rate(0.01))
print(TrainingRun.validate_learning_rate(1.5))



# Run count: 3
# Model-A training started.
# Model: Model-A
# Learning Rate: 0.01
# Status: Running
# Model: Model-D
# Learning Rate: 0.02
# Status: Not Started
# True
# False
