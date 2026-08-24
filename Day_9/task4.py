# POLYMORPHISM

class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

    def summary(self):
        return f"Model: {self.model_name}, LR: {self.learning_rate}"


class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):
        return f"{super().summary()}, Schedule: {self.schedule}"


class EarlyStoppingRun(TrainingRun):
    def __init__(self, model_name, learning_rate, patience):
        super().__init__(model_name, learning_rate)
        self.patience = patience

    def summary(self):
        return f"{super().summary()}, Patience: {self.patience}"


def print_all_summaries(runs):
    for run in runs:
        print(run.summary())


runs = [
    TrainingRun("GPT-Mini", 0.01),
    LRSchedulerRun("GPT-Scheduler", 0.01, [0.01, 0.005]),
    EarlyStoppingRun("GPT-Early", 0.01, 5)
]

print_all_summaries(runs)

# Output:
# Model: GPT-Mini, LR: 0.01
# Model: GPT-Scheduler, LR: 0.01, Schedule: [0.01, 0.005]
# Model: GPT-Early, LR: 0.01, Patience: 5