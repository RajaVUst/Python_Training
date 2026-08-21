
class TrainingRun:

    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "pending"

        TrainingRun.run_count += 1

    def start(self):
        self.status = "running"

    def summary(self):
        print(f"Model: {self.model_name}")
        print(f"Learning Rate: {self.learning_rate}")
        print(f"Status: {self.status}")


class LRSchedulerRun(TrainingRun):

    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):

        super().summary()
        print(f"Learning Rate Schedule: {self.schedule}")

run = LRSchedulerRun(
    "GPT-Mini",
    0.01,
    [0.01, 0.005, 0.001]
)

run.summary()

print("Total Training Runs:", TrainingRun.run_count)


# OUTPUT:
# Model: GPT-Mini
# Learning Rate: 0.01
# Status: pending
# Learning Rate Schedule: [0.01, 0.005, 0.001]
# Total Training Runs: 1
