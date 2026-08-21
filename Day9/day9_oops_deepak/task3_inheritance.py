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
        base = super().summary()          
        return f"{base}, schedule={self.schedule}"


sched_run = LRSchedulerRun("gpt-sched", 0.01, schedule=[0.01, 0.008, 0.005])
print(sched_run.summary())
print(TrainingRun.run_count)

# Output:
# [gpt-sched] lr=0.01, status=pending, schedule=[0.01, 0.008, 0.005]
# 1