class TrainingRun:
    run_count = 0 

    def __init__(self, model_name, learning_rate):
        self._validate_lr(learning_rate)
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"
        TrainingRun.run_count += 1

    def start(self):
        self._status = "running"

    def summary(self):
        return f"[{self.model_name}] lr={self.learning_rate}, status={self._status}"

    @classmethod
    def from_config(cls, config_dict):
        return cls(config_dict["model_name"], config_dict["learning_rate"])

    @staticmethod
    def _validate_lr(lr):
        if not (0 < lr < 1):
            raise ValueError("learning_rate must be between 0 and 1")


r1 = TrainingRun("gpt-mini", 0.01)
r2 = TrainingRun("gpt-nano", 0.05)
r3 = TrainingRun.from_config({"model_name": "gpt-pico", "learning_rate": 0.02})

print(TrainingRun.run_count)
print(r1.learning_rate, r2.learning_rate)

# Output:
# 3
# 0.01 0.05