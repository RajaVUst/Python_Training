# Task 4 - Add a Dunder
# Adds __str__, __repr__, and __eq__ to TrainingRun.

# __str__  → human-readable output, used by print()       — like Java's toString()
# __repr__ → developer-facing output, used in REPL/logs   — also like toString() but for debugging
# __eq__   → equality check with ==                       — like Java's equals()

class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.is_running = False
        TrainingRun.run_count += 1

    def start(self):
        self.is_running = True

    def summary(self):
        status = "Running" if self.is_running else "Not started"
        print(f"Model: {self.model_name} | LR: {self.learning_rate} | Status: {status}")

    @classmethod
    def from_config(cls, config_dict):
        return cls(config_dict["model_name"], config_dict["learning_rate"])

    @staticmethod
    def validate_lr(lr):
        if not (0 < lr < 1):
            raise ValueError(f"Learning rate must be between 0 and 1, got {lr}")

    def __str__(self):
        # clean, user-friendly string — shown by print()
        return f"TrainingRun(model='{self.model_name}', lr={self.learning_rate})"

    def __repr__(self):
        # developer-oriented string — shown in REPL and logs
        return f"TrainingRun(model_name='{self.model_name}', learning_rate={self.learning_rate})"

    def __eq__(self, other):
        # two runs are equal if they have the same model name and learning rate
        if not isinstance(other, TrainingRun):
            return False
        return self.model_name == other.model_name and self.learning_rate == other.learning_rate


# --- Demo ---
run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("gpt-mini", 0.01)
run3 = TrainingRun("bert-base", 0.001)

print(run1)              # uses __str__  → TrainingRun(model='gpt-mini', lr=0.01)
print(repr(run1))        # uses __repr__ → TrainingRun(model_name='gpt-mini', learning_rate=0.01)

print(run1 == run2)      # True  — same model_name and learning_rate
print(run1 == run3)      # False — different model and lr
