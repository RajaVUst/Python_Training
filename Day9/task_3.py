class TrainingRun:

    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "pending"

        TrainingRun.run_count += 1

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

        if self.schedule:
            print(f"Current Scheduled Learning Rate: {self.schedule[0]}")


run1 = TrainingRun("GPT-Model", 0.01)

run2 = LRSchedulerRun(
    "BERT-Model",
    0.01,
    [0.01, 0.005, 0.001]
)

print("TrainingRun count:", TrainingRun.run_count)

print("\nNormal Training Run:")
run1.summary()

print("\nLR Scheduler Run:")
run2.summary()





# Normal Training Run:
# Model: GPT-Model
# Learning Rate: 0.01
# Status: pending

# LR Scheduler Run:
# Model: BERT-Model
# Learning Rate: 0.01
# Status: pending
# Learning Rate Schedule: [0.01, 0.005, 0.001]
# Current Scheduled Learning Rate: 0.01
