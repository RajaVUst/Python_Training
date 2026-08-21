
class TrainingRun:

    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "pending"

        TrainingRun.run_count += 1

    def summary(self):
        print(
            f"TrainingRun: {self.model_name}, "
            f"LR: {self.learning_rate}, "
            f"Status: {self.status}"
        )

class LRSchedulerRun(TrainingRun):

    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):
        print(
            f"LRSchedulerRun: {self.model_name}, "
            f"Current LR: {self.schedule[0]}, "
            f"Schedule: {self.schedule}"
        )

class EarlyStoppingRun(TrainingRun):

    def __init__(self, model_name, learning_rate, patience):
        super().__init__(model_name, learning_rate)
        self.patience = patience

    def summary(self):
        print(
            f"EarlyStoppingRun: {self.model_name}, "
            f"LR: {self.learning_rate}, "
            f"Patience: {self.patience}"
        )

def print_all_summaries(runs):

    for run in runs:
        run.summary()

run1 = TrainingRun("GPT-Mini", 0.01)

run2 = LRSchedulerRun(
    "BERT",
    0.001,
    [0.001, 0.0005, 0.0001]
)

run3 = EarlyStoppingRun(
    "ResNet",
    0.05,
    5
)

runs = [run1, run2, run3]

print_all_summaries(runs)


# OUTPUT:
# TrainingRun: GPT-Mini, LR: 0.01, Status: pending
# LRSchedulerRun: BERT, Current LR: 0.001, Schedule: [0.001, 0.0005, 0.0001]
# EarlyStoppingRun: ResNet, LR: 0.05, Patience: 5