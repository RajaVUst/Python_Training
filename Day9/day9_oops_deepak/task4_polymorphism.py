class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"
        TrainingRun.run_count += 1

    def summary(self):
        return f"[{self.model_name}] lr={self.learning_rate}, status={self._status}"


class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):
        return f"{super().summary()}, schedule={self.schedule}"


class EarlyStoppingRun(TrainingRun):
    def __init__(self, model_name, learning_rate, patience):
        super().__init__(model_name, learning_rate)
        self.patience = patience

    def summary(self):
        return f"{super().summary()}, patience={self.patience}"


def print_all_summaries(runs):
    for run in runs:
        print(run.summary())


r1 = TrainingRun("gpt-mini", 0.01)
sched_run = LRSchedulerRun("gpt-sched", 0.01, schedule=[0.01, 0.008, 0.005])
stop_run = EarlyStoppingRun("gpt-early", 0.01, patience=3)

print_all_summaries([r1, sched_run, stop_run])

# Output:
# [gpt-mini] lr=0.01, status=pending
# [gpt-sched] lr=0.01, status=pending, schedule=[0.01, 0.008, 0.005]
# [gpt-early] lr=0.01, status=pending, patience=3