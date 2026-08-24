# DESIGN A CLASS

class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        TrainingRun.run_count += 1

    @classmethod
    def from_config(cls, config):
        return cls(config["model_name"], config["learning_rate"])

    def start(self):
        print(f"Training started for {self.model_name}")

    def summary(self):
        return f"Model: {self.model_name}, LR: {self.learning_rate}"


run1 = TrainingRun("GPT-Mini", 0.01)
run2 = TrainingRun("BERT", 0.001)
run3 = TrainingRun.from_config(
    {"model_name": "Llama", "learning_rate": 0.005}
)

print(run1.summary())
print(run2.summary())
print(run3.summary())
print("Run Count:", TrainingRun.run_count)

# Output:
# Model: GPT-Mini, LR: 0.01
# Model: BERT, LR: 0.001
# Model: Llama, LR: 0.005
# Run Count: 3
