# Task 2 - Extend It
# LRSchedulerRun inherits from TrainingRun and adds a per-epoch learning rate schedule.

from task_1 import TrainingRun


class LRSchedulerRun(TrainingRun):

    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)  # reuse parent constructor
        self.schedule = schedule  # list of lr values per epoch e.g. [0.01, 0.005, 0.001]

    def summary(self):
        super().summary()  # call parent summary — no copy-paste
        print(f"Schedule: {self.schedule} | Current LR: {self.schedule[0] if self.schedule else 'N/A'}")


# --- Demo ---
run1 = LRSchedulerRun("gpt-mini", 0.01, [0.01, 0.005, 0.001])
run2 = LRSchedulerRun("bert-base", 0.001, [0.001, 0.0005])

print(f"Total runs created: {TrainingRun.run_count}")  # counts both LRSchedulerRun instances too

run1.summary()
print("---")
run2.summary()
