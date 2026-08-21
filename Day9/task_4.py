class TrainingRun:
    def __init__(self, model_name, epochs):
        self.model_name = model_name
        self.epochs = epochs

    def summary(self):
        print(f"TrainingRun: {self.model_name}, Epochs: {self.epochs}")


class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, epochs, schedule):
        super().__init__(model_name, epochs)
        self.schedule = schedule

    def summary(self):
        print(
            f"LRSchedulerRun: {self.model_name}, "
            f"Epochs: {self.epochs}, "
            f"Learning Rate Schedule: {self.schedule}"
        )


class EarlyStoppingRun(TrainingRun):
    def __init__(self, model_name, epochs, patience):
        super().__init__(model_name, epochs)
        self.patience = patience

    def summary(self):
        print(
            f"EarlyStoppingRun: {self.model_name}, "
            f"Epochs: {self.epochs}, "
            f"Patience: {self.patience}"
        )


def print_all_summaries(runs):
    for run in runs:
        run.summary()


run1 = TrainingRun("ResNet", 10)

run2 = LRSchedulerRun(
    "VGG16",
    20,
    [0.1, 0.01, 0.001]
)

run3 = EarlyStoppingRun(
    "BERT",
    15,
    3
)


runs = [run1, run2, run3]

print_all_summaries(runs)



# TrainingRun: ResNet, Epochs: 10
# LRSchedulerRun: VGG16, Epochs: 20, Learning Rate Schedule: [0.1, 0.01, 0.001]
# EarlyStoppingRun: BERT, Epochs: 15, Patience: 3