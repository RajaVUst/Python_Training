# Task 4 - Polymorphism
class TrainingRun:
    run_count = 0
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        TrainingRun.run_count += 1
    def summary(self):
        print(f"Model Name    : {self.model_name}")
        print(f"Learning Rate : {self.learning_rate}")

class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule
    def summary(self):
        super().summary()
        print(f"Schedule      : {self.schedule}")

class EarlyStoppingRun(TrainingRun):
    def __init__(self, model_name, learning_rate, patience):
        super().__init__(model_name, learning_rate)
        self.patience = patience
    def summary(self):
        super().summary()
        print(f"Patience      : {self.patience} epochs")

def print_all_summaries(runs):
    for run in runs:
        print("-" * 30)
        run.summary()
        print()

run1 = TrainingRun("gpt-mini", 0.01)
run2 = LRSchedulerRun(
    "gpt-large",
    0.001,
    [0.001, 0.0005, 0.0001]
)
run3 = EarlyStoppingRun(
    "bert-base",
    0.005,
    5
)
runs = [run1, run2, run3]
print_all_summaries(runs)
print("Total Runs Created:", TrainingRun.run_count)

#Output
'''
Model Name    : gpt-mini
Learning Rate : 0.01

Model Name    : gpt-large
Learning Rate : 0.001
Schedule      : [0.001, 0.0005, 0.0001]

Model Name    : bert-base
Learning Rate : 0.005
Patience      : 5 epochs

Total Runs Created: 3
'''