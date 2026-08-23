class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"

        TrainingRun.run_count += 1

    def start(self):
        self._status = "running"

    def summary(self):
        return (
            f"Model: {self.model_name}, "
            f"Learning rate: {self.learning_rate}, "
            f"Status: {self._status}"
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
        self.current_epoch = 0

    def summary(self):
        parent_summary = super().summary()

        if self.schedule:
            current_lr = self.schedule[self.current_epoch]
        else:
            current_lr = self.learning_rate

        return (
            f"{parent_summary}, "
            f"Schedule: {self.schedule}, "
            f"Current scheduled LR: {current_lr}"
        )


normal_run = TrainingRun(
    "gpt-mini",
    0.01
)

scheduled_run = LRSchedulerRun(
    "bert-small",
    0.01,
    [0.01, 0.005, 0.001]
)

print(normal_run.summary())
print(scheduled_run.summary())

print("Total runs:", TrainingRun.run_count)