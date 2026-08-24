# Design a class with a constructor, attributes and methods
class TrainingRun:
    run_count = 0
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "pending"
        TrainingRun.run_count += 1

    def start(self):
        self.status = "running"
        print("Training started")

    def summary(self):
        print("Model:", self.model_name)
        print("Learning Rate:", self.learning_rate)
        print("Status:", self.status)

    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )


#objects
run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("bert", 0.02)
run3 = TrainingRun("llama", 0.03)
print("Run count:", TrainingRun.run_count)

run1.start()
run1.summary()

# using dictionary
config = {
    "model_name": "transformer",
    "learning_rate": 0.05
}

run4 = TrainingRun.from_config(config)
run4.summary()


# Output:
# Run count: 3
# Training started
# Model: gpt-mini
# Learning Rate: 0.01
# Status: running
# Model: transformer
# Learning Rate: 0.05
# Status: pending