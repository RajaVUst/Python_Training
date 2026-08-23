class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

    def summary(self):
        return (
            f"Model: {self.model_name}, "
            f"Learning Rate: {self.learning_rate}"
        )


class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):
        parent_summary = super().summary()
        return (
            f"{parent_summary}, "
            f"Schedule: {self.schedule}"
        )


class EarlyStoppingRun(TrainingRun):
    def __init__(self, model_name, learning_rate, patience):
        super().__init__(model_name, learning_rate)
        self.patience = patience

    def summary(self):
        parent_summary = super().summary()
        return (
            f"{parent_summary}, "
            f"Patience: {self.patience} epochs"
        )


def print_all_summaries(runs):
    for run in runs:
        print(run.summary())


run1 = TrainingRun("ResNet50", 0.01)

run2 = LRSchedulerRun(
    "BERT",
    0.001,
    [0.001, 0.0005, 0.0001]
)

run3 = EarlyStoppingRun(
    "XGBoost",
    0.1,
    5
)
runs = [run1, run2, run3]
print_all_summaries(runs)