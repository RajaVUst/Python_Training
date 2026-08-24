# INHERITANCE

class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        TrainingRun.run_count += 1

    def summary(self):
        return f"Model: {self.model_name}, LR: {self.learning_rate}"


class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):
        return f"{super().summary()}, Schedule: {self.schedule}"


run = LRSchedulerRun(
    "GPT-Scheduler",
    0.01,
    [0.01, 0.005, 0.001]
)

print(run.summary())
print("Run Count:", TrainingRun.run_count)

# Output:
# Model: GPT-Scheduler, LR: 0.01, Schedule: [0.01, 0.005, 0.001]
# Run Count: 1