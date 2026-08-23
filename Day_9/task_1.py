class TrainingRun:

    run_count = 0

    def __init__(self, model_name, learning_rate):
        if not self.validate_learning_rate(learning_rate):
            raise ValueError("Learning rate must be between 0 and 1.")

        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "Not Started"

        TrainingRun.run_count += 1

    def start(self):
        self.status = "Running"
        print(f"Training started for {self.model_name}")

    def summary(self):
        return (
            f"Model: {self.model_name}, "
            f"Learning Rate: {self.learning_rate}, "
            f"Status: {self.status}"
        )

    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )

    @staticmethod
    def validate_learning_rate(lr):
        return 0 < lr < 1


run1 = TrainingRun("ResNet50", 0.01)
run2 = TrainingRun("BERT", 0.001)

config = {
    "model_name": "XGBoost",
    "learning_rate": 0.1
}
run3 = TrainingRun.from_config(config)

run1.start()

print(run1.summary())
print(run2.summary())
print(run3.summary())
print("Total runs created:", TrainingRun.run_count)

