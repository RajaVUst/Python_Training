#  Implement inheritance and method overriding

class TrainingRun:
    run_count = 0
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "pending"
        TrainingRun.run_count += 1

    def summary(self):
        print("Model:", self.model_name)
        print("Learning Rate:", self.learning_rate)
        print("Status:", self.status)

class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):
        super().summary()
        print("Schedule:", self.schedule)

run = LRSchedulerRun(
    "gpt-mini",
    0.01,
    [0.01, 0.005, 0.001]
)
run.summary()
print("Run count:", TrainingRun.run_count)


# Output:
# Model: gpt-mini
# Learning Rate: 0.01
# Status: pending
# Schedule: [0.01, 0.005, 0.001]
# Run count: 1