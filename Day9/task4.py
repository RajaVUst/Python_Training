#  Use polymorphism to treat different subclasses interchangeably

class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

    def summary(self):
        print("Model:", self.model_name)
        print("Learning Rate:", self.learning_rate)

class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):
        super().summary()
        print("Schedule:", self.schedule)

class EarlyStoppingRun(TrainingRun):
    def __init__(self, model_name, learning_rate, patience):
        super().__init__(model_name, learning_rate)
        self.patience = patience
    def summary(self):
        super().summary()
        print("Patience:", self.patience)

def print_all_summaries(runs):
    for run in runs:
        run.summary()

run1 = TrainingRun("gpt-mini", 0.01)
run2 = LRSchedulerRun(
    "bert",
    0.02,
    [0.02, 0.01, 0.005]
)

run3 = EarlyStoppingRun(
    "llama",
    0.03,
    5
)
runs = [run1, run2, run3]
print_all_summaries(runs)

# Output:
# Model: gpt-mini
# Learning Rate: 0.01
# Model: bert
# Learning Rate: 0.02
# Schedule: [0.02, 0.01, 0.005]
# Model: llama
# Learning Rate: 0.03
# Patience: 5