# Task 3 - Inheritance

class TrainingRun:
    # Class attribute shared by all instances
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

        TrainingRun.run_count += 1

    def summary(self):
        print(f"Model Name    : {self.model_name}")
        print(f"Learning Rate : {self.learning_rate}")


# Subclass

class LRSchedulerRun(TrainingRun):

    def __init__(self, model_name, learning_rate, schedule):
        # Reuse parent constructor
        super().__init__(model_name, learning_rate)

        # New attribute specific to this subclass
        self.schedule = schedule

    def summary(self):
        # Call parent implementation
        super().summary()

        # Add subclass-specific information
        if self.schedule:
            print(f"Current Scheduled LR : {self.schedule[0]}")
            print(f"Schedule             : {self.schedule}")
        else:
            print("Schedule             : []")


# Testing

run1 = TrainingRun("gpt-mini", 0.01)

run2 = LRSchedulerRun(
    "gpt-large",
    0.001,
    [0.001, 0.0005, 0.0001]
)

print("Training Run Summary")
run1.summary()

print("\nLRSchedulerRun Summary")
run2.summary()

print("\nTotal Runs Created:")
print(TrainingRun.run_count)

#Output
'''Training Run Summary
Model Name    : gpt-mini
Learning Rate : 0.01

LRSchedulerRun Summary
Model Name    : gpt-large
Learning Rate : 0.001
Current Scheduled LR : 0.001
Schedule             : [0.001, 0.0005, 0.0001]

Total Runs Created:
2
'''