from abc import ABC, abstractmethod



class TrainingRun:

    run_count = 0

    def __init__(self, model_name, learning_rate):

        if not self.validate_learning_rate(learning_rate):
            raise ValueError("Learning rate must be between 0 and 1.")

        self.model_name = model_name
        self.learning_rate = learning_rate

        self._status = "pending"

        self.__api_key = "fake-training-api-key"

        TrainingRun.run_count = TrainingRun.run_count + 1


    @staticmethod
    def validate_learning_rate(learning_rate):

        return 0 < learning_rate < 1


    def start(self):

        self.status = "running"

        print(f"{self.model_name} training started.")


    def summary(self):

        print(
            f"Model: {self.model_name}, "
            f"Learning Rate: {self.learning_rate}, "
            f"Status: {self.status}"
        )


    @property
    def status(self):

        return self._status


    @status.setter
    def status(self, value):

        if value not in ["pending", "running", "done"]:
            raise ValueError(
                "Status must be pending, running, or done."
            )

        self._status = value


    @classmethod
    def from_config(cls, config_dict):

        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )


    def __str__(self):

        return (
            f"TrainingRun("
            f"model='{self.model_name}', "
            f"lr={self.learning_rate})"
        )


    def __eq__(self, other):

        if not isinstance(other, TrainingRun):
            return False

        return (
            self.model_name == other.model_name
            and self.learning_rate == other.learning_rate
        )


    def __repr__(self):

        return (
            f"TrainingRun("
            f"model_name='{self.model_name}', "
            f"learning_rate={self.learning_rate})"
        )


run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("bert-base", 0.05)
run3 = TrainingRun("resnet", 0.001)

print("Task 1:")
print("Run count:", TrainingRun.run_count)
# Output: Run count: 3

print(run1.model_name)
# Output: gpt-mini

print(run2.learning_rate)
# Output: 0.05


config = {
    "model_name": "gpt-config",
    "learning_rate": 0.02
}

run4 = TrainingRun.from_config(config)

print("\nFrom config:")
print(run4)
# Output: TrainingRun(model='gpt-config', lr=0.02)


print("\nStarting run:")

run1.start()
# Output: gpt-mini training started.

run1.summary()
# Output: Model: gpt-mini, Learning Rate: 0.01, Status: running


# Task 2: Encapsulation

print("\nTask 2:")

print("Current status:", run1.status)
# Output: Current status: running


run1.status = "done"

print("New status:", run1.status)
# Output: New status: done



try:

    run1.status = "paused"

except ValueError as error:

    print("Error:", error)

# Output:
# Error: Status must be pending, running, or done.



try:

    print(run1.__api_key)

except AttributeError:

    print("Direct access to __api_key is not allowed.")

# Output:
# Direct access to __api_key is not allowed.

print(run1._TrainingRun__api_key)
# Output: fake-training-api-key


# Task 3: Inheritance

class LRSchedulerRun(TrainingRun):

    def __init__(self, model_name, learning_rate, schedule):

        # Reuse parent constructor
        super().__init__(model_name, learning_rate)

        self.schedule = schedule


    # Override summary()
    def summary(self):

        # Call parent summary()
        super().summary()

        print("Learning rate schedule:", self.schedule)

        if len(self.schedule) > 0:
            print("Current scheduled learning rate:", self.schedule[0])



scheduler_run = LRSchedulerRun(
    "gpt-scheduler",
    0.01,
    [0.01, 0.008, 0.005]
)


print("\nTask 3:")

scheduler_run.summary()

# Output:
# Model: gpt-scheduler, Learning Rate: 0.01, Status: pending
# Learning rate schedule: [0.01, 0.008, 0.005]
# Current scheduled learning rate: 0.01


print("Run count:", TrainingRun.run_count)
# Output: Run count: 5


# Task 4: Polymorphism

class EarlyStoppingRun(TrainingRun):

    def __init__(self, model_name, learning_rate, patience):

        super().__init__(model_name, learning_rate)

        self.patience = patience


    def summary(self):

        super().summary()

        print("Patience:", self.patience)



normal_run = TrainingRun(
    "normal-model",
    0.01
)

scheduler_run2 = LRSchedulerRun(
    "scheduled-model",
    0.02,
    [0.02, 0.01, 0.005]
)

early_stop_run = EarlyStoppingRun(
    "early-stop-model",
    0.03,
    5
)



def print_all_summaries(runs):

    for run in runs:

        run.summary()


runs = [
    normal_run,
    scheduler_run2,
    early_stop_run
]

print("\nTask 4:")

print_all_summaries(runs)

# Output:
#
# Model: normal-model, Learning Rate: 0.01, Status: pending
#
# Model: scheduled-model, Learning Rate: 0.02, Status: pending
# Learning rate schedule: [0.02, 0.01, 0.005]
# Current scheduled learning rate: 0.02
#
# Model: early-stop-model, Learning Rate: 0.03, Status: pending
# Patience: 5


# Task 5: Duck Typing
class Cleaner:

    def process(self, data):

        return data.strip()


class Tokenizer:

    def process(self, data):

        return data.split()


class Normalizer:

    def process(self, data):

        if isinstance(data, list):
            return [word.lower() for word in data]

        return data.lower()


def run_pipeline(steps, data):

    for step in steps:

        data = step.process(data)

    return data


print("\nTask 5 - Duck Typing:")

steps = [
    Cleaner(),
    Tokenizer(),
    Normalizer()
]

result = run_pipeline(
    steps,
    "  HELLO PYTHON WORLD  "
)

print(result)
# Output: ['hello', 'python', 'world']

# Task 5: ABC Version


class Step(ABC):

    @abstractmethod
    def process(self, data):

        pass


class CleanerABC(Step):

    def process(self, data):

        return data.strip()


class TokenizerABC(Step):

    def process(self, data):

        return data.split()


class NormalizerABC(Step):

    def process(self, data):

        return [word.lower() for word in data]


def run_pipeline_abc(steps, data):

    for step in steps:

        data = step.process(data)

    return data


print("\nABC Version:")

abc_steps = [
    CleanerABC(),
    TokenizerABC(),
    NormalizerABC()
]

result = run_pipeline_abc(
    abc_steps,
    "  HELLO PYTHON WORLD  "
)

print(result)
# Output: ['hello', 'python', 'world']


# Step itself cannot be instantiated

try:

    step = Step()

except TypeError:

    print("Step cannot be instantiated directly.")

# Output:
# Step cannot be instantiated directly.


# Duck typing is useful when classes only need to follow the
# same method behavior without needing a common parent class.
#
# ABCs are useful when a team wants to explicitly define and
# enforce a common contract for related classes.

# Task 6: Dunder Methods

print("\nTask 6:")

run_a = TrainingRun(
    "gpt-mini",
    0.01
)

run_b = TrainingRun(
    "gpt-mini",
    0.01
)

run_c = TrainingRun(
    "bert",
    0.05
)



print(run_a)

# Output:
# TrainingRun(model='gpt-mini', lr=0.01)



print(repr(run_a))

# Output:
# TrainingRun(model_name='gpt-mini', learning_rate=0.01)


# __eq__

print(run_a == run_b)

# Output:
# True


print(run_a == run_c)

# Output:
# False
print("\nFinal run count:")

print(TrainingRun.run_count)

# Output:
# Final run count: 11
#
# Note:
# The exact final count depends on how many TrainingRun objects
# were created throughout this script.
