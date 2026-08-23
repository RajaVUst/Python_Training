class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"

        TrainingRun.run_count += 1

    def summary(self):
        return (
            f"TrainingRun: model={self.model_name}, "
            f"lr={self.learning_rate}, "
            f"status={self._status}"
        )


class LRSchedulerRun(TrainingRun):

    def __init__(
        self,
        model_name,
        learning_rate,
        schedule
    ):
        super().__init__(
            model_name,
            learning_rate
        )

        self.schedule = schedule

    def summary(self):
        return (
            f"{super().summary()}, "
            f"schedule={self.schedule}"
        )


class EarlyStoppingRun(TrainingRun):

    def __init__(
        self,
        model_name,
        learning_rate,
        patience
    ):
        super().__init__(
            model_name,
            learning_rate
        )

        self.patience = patience

    def summary(self):
        return (
            f"{super().summary()}, "
            f"early-stopping patience={self.patience}"
        )


def print_all_summaries(runs):
    for run in runs:
        print(run.summary())


runs = [
    TrainingRun(
        "gpt-mini",
        0.01
    ),
    LRSchedulerRun(
        "bert-small",
        0.001,
        [0.001, 0.0005, 0.0001]
    ),
    EarlyStoppingRun(
        "resnet",
        0.05,
        3
    )
]

print_all_summaries(runs)

#output
'''
TrainingRun: model=gpt-mini, lr=0.01, status=pending
TrainingRun: model=bert-small, lr=0.001, status=pending, schedule=[0.001, 0.0005, 0.0001]
TrainingRun: model=resnet, lr=0.05, status=pending, early-stopping patience=3
'''