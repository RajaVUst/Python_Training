class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"

        TrainingRun.run_count += 1

    def summary(self):
        return (
            f"Model: {self.model_name}, "
            f"Learning Rate: {self.learning_rate}, "
            f"Status: {self._status}"
        )


class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
    
        super().__init__(model_name, learning_rate)

        self.schedule = schedule

    def summary(self):
        parent_summary = super().summary()

        current_lr = (
            self.schedule[0]
            if self.schedule else self.learning_rate
        )

        return (
            f"{parent_summary}, "
            f"Current Scheduled LR: {current_lr}"
        )

run1 = TrainingRun("ResNet50", 0.01)

scheduler_run = LRSchedulerRun(
    "BERT",
    0.001,
    [0.001, 0.0005, 0.0001]
)

print(run1.summary())
print(scheduler_run.summary())

print("Total runs created:", TrainingRun.run_count)
