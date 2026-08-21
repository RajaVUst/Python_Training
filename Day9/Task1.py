
class TrainingRun:

    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "pending"

        if not self.validate_learning_rate(learning_rate):
            raise ValueError("Learning rate must be between 0 and 1")

        TrainingRun.run_count += 1


    def start(self):
        self.status = "running"
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
    def validate_learning_rate(lr):
        return 0 < lr < 1


run1 = TrainingRun("GPT-Mini", 0.01)
run2 = TrainingRun("BERT", 0.001)
run3 = TrainingRun("ResNet", 0.05)

run1.start()
run1.summary()

print("Total Training Runs:", TrainingRun.run_count)


config = {
    "model_name": "Llama",
    "learning_rate": 0.02
}

run4 = TrainingRun.from_config(config)

print("\nObject created using from_config:")
run4.summary()

# OUTPUT:
# GPT-Mini training started.
# Model: GPT-Mini
# Learning Rate: 0.01
# Status: running
# Total Training Runs: 3

# Object created using from_config:
# Model: Llama
# Learning Rate: 0.02
# Status: pending