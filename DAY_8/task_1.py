# Task 1 - Design a Class
# TrainingRun represents a single model-training run.

class TrainingRun:
    run_count = 0  # class attribute: shared across all instances (like Java 'static')

    def __init__(self, model_name, learning_rate):
        TrainingRun.validate_lr(learning_rate)  # stretch goal: validate lr in __init__
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.is_running = False
        TrainingRun.run_count += 1  # increment shared counter on every new instance

    def start(self):
        self.is_running = True
        print(f"Run started: {self.model_name} with lr={self.learning_rate}")

    def summary(self):
        status = "Running" if self.is_running else "Not started"
        print(f"Model: {self.model_name} | LR: {self.learning_rate} | Status: {status}")

    @classmethod
    def from_config(cls, config_dict):
        # alternate constructor — like a static factory method in Java
        return cls(config_dict["model_name"], config_dict["learning_rate"])

    @staticmethod
    def validate_lr(lr):
        # stretch goal: reject learning rates outside a sane range
        if not (0 < lr < 1):
            raise ValueError(f"Learning rate must be between 0 and 1, got {lr}")


# --- Demo ---
run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("bert-base", 0.001)
run3 = TrainingRun.from_config({"model_name": "llama", "learning_rate": 0.005})

print(f"Total runs created: {TrainingRun.run_count}")  # should be 3

run1.start()
run1.summary()
run2.summary()
