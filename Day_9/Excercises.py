
# ============================================================
# TASK 1 - DESIGN A CLASS
# ============================================================

class TrainingRun:

    # Class attribute
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"

        # Private attribute
        self.__api_key = "fake-api-key-123"

        TrainingRun.run_count += 1

    def start(self):
        self.status = "running"
        print(self.model_name, "started")

    def summary(self):
        print("Model:", self.model_name)
        print("Learning Rate:", self.learning_rate)
        print("Status:", self.status)

    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )

    @staticmethod
    def validate_learning_rate(lr):
        return 0 < lr < 1


# Create objects
run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("bert", 0.02)
run3 = TrainingRun("llama", 0.03)

print("Run count:", TrainingRun.run_count)

run1.start()
run1.summary()

# Create object using class method
config = {
    "model_name": "roberta",
    "learning_rate": 0.05
}

run4 = TrainingRun.from_config(config)

print("Created using from_config:")
run4.summary()


# SAMPLE OUTPUT:
#
# Run count: 3
# gpt-mini started
# Model: gpt-mini
# Learning Rate: 0.01
# Status: running
# Created using from_config:
# Model: roberta
# Learning Rate: 0.05
# Status: pending


# ============================================================
# TASK 2 - ENCAPSULATION
# ============================================================

print("\n--- TASK 2 ---")

# Property getter
# and setter are added to TrainingRun here.

# Add property dynamically for simple demonstration
def get_status(self):
    return self._status


def set_status(self, value):

    if value not in ["pending", "running", "done"]:
        raise ValueError("Invalid status")

    self._status = value


TrainingRun.status = property(get_status, set_status)


run = TrainingRun("test-model", 0.01)

run.status = "running"

print("Status:", run.status)

# Invalid status
try:
    run.status = "paused"
except ValueError as e:
    print("Error:", e)

# Private variable cannot be accessed directly
try:
    print(run.__api_key)
except AttributeError:
    print("Direct access to __api_key failed")

# Name mangling
print("Private API key:", run._TrainingRun__api_key)


# SAMPLE OUTPUT:
#
# --- TASK 2 ---
# Status: running
# Error: Invalid status
# Direct access to __api_key failed
# Private API key: fake-api-key-123
#
# Python's private variables are not strictly private like Java.
# Python mainly trusts the developer to follow the naming convention.


# ============================================================
# TASK 3 - INHERITANCE
# ============================================================

print("\n--- TASK 3 ---")


class LRSchedulerRun(TrainingRun):

    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):

        # Call parent method
        super().summary()

        print("Schedule:", self.schedule)


schedule = [0.1, 0.05, 0.01]

lr_run = LRSchedulerRun(
    "gpt-scheduler",
    0.1,
    schedule
)

lr_run.summary()

print("Total runs:", TrainingRun.run_count)


# SAMPLE OUTPUT:
#
# --- TASK 3 ---
# Model: gpt-scheduler
# Learning Rate: 0.1
# Status: pending
# Schedule: [0.1, 0.05, 0.01]
# Total runs: 5


# ============================================================
# TASK 4 - POLYMORPHISM
# ============================================================

print("\n--- TASK 4 ---")


class EarlyStoppingRun(TrainingRun):

    def __init__(self, model_name, learning_rate, patience):
        super().__init__(model_name, learning_rate)
        self.patience = patience

    def summary(self):
        print("Model:", self.model_name)
        print("Learning Rate:", self.learning_rate)
        print("Patience:", self.patience)


def print_all_summaries(runs):

    for run in runs:
        run.summary()


# Create different objects
normal_run = TrainingRun("normal-model", 0.01)

scheduler_run = LRSchedulerRun(
    "scheduler-model",
    0.1,
    [0.1, 0.05, 0.01]
)

early_run = EarlyStoppingRun(
    "early-model",
    0.02,
    5
)

# Mixed list
runs = [
    normal_run,
    scheduler_run,
    early_run
]

print_all_summaries(runs)


# SAMPLE OUTPUT:
#
# --- TASK 4 ---
# Model: normal-model
# Learning Rate: 0.01
# Status: pending
#
# Model: scheduler-model
# Learning Rate: 0.1
# Status: pending
# Schedule: [0.1, 0.05, 0.01]
#
# Model: early-model
# Learning Rate: 0.02
# Patience: 5
#
# Notice:
# print_all_summaries() does not use isinstance()
# or type(). Each object automatically calls
# its own summary() method.


# ============================================================
# TASK 5 - DUCK TYPING
# ============================================================

print("\n--- TASK 5 - DUCK TYPING ---")


class Cleaner:

    def process(self, data):
        return data.strip()


class Tokenizer:

    def process(self, data):
        return data.split()


class Normalizer:

    def process(self, data):
        return str(data).lower()


def run_pipeline(steps, data):

    for step in steps:
        data = step.process(data)

    return data


steps = [
    Cleaner(),
    Tokenizer(),
]

data = "  Hello Python  "

result = run_pipeline(steps, data)

print("Duck typing result:", result)


# SAMPLE OUTPUT:
#
# --- TASK 5 - DUCK TYPING ---
# Duck typing result: ['Hello', 'Python']


# ============================================================
# TASK 5 - ABSTRACT BASE CLASS
# ============================================================

print("\n--- TASK 5 - ABC ---")

from abc import ABC, abstractmethod


class Step(ABC):

    @abstractmethod
    def process(self, data):
        pass


class ABCCleaner(Step):

    def process(self, data):
        return data.strip()


class ABCTokenizer(Step):

    def process(self, data):
        return data.split()


class ABCNormalizer(Step):

    def process(self, data):
        return str(data).lower()


def run_abc_pipeline(steps, data):

    for step in steps:
        data = step.process(data)

    return data


abc_steps = [
    ABCCleaner(),
    ABCTokenizer()
]

result = run_abc_pipeline(
    abc_steps,
    "  Hello Python  "
)

print("ABC result:", result)

# Step itself cannot be created
try:
    Step()
except TypeError:
    print("Step() cannot be instantiated")


# SAMPLE OUTPUT:
#
# --- TASK 5 - ABC ---
# ABC result: ['Hello', 'Python']
# Step() cannot be instantiated
#
# Duck typing is simple and flexible.
# ABCs are useful when a team wants to clearly enforce
# that every class follows the same contract.


# ============================================================
# TASK 6 - DUNDER METHODS
# ============================================================

print("\n--- TASK 6 ---")


# Add __str__ and __eq__ to TrainingRun

def training_run_str(self):
    return (
        f"TrainingRun(model='{self.model_name}', "
        f"lr={self.learning_rate})"
    )


def training_run_eq(self, other):

    if not isinstance(other, TrainingRun):
        return False

    return (
        self.model_name == other.model_name
        and self.learning_rate == other.learning_rate
    )


TrainingRun.__str__ = training_run_str
TrainingRun.__eq__ = training_run_eq


run_a = TrainingRun("gpt-mini", 0.01)
run_b = TrainingRun("gpt-mini", 0.01)
run_c = TrainingRun("bert", 0.02)

print(run_a)

print("run_a == run_b:", run_a == run_b)
print("run_a == run_c:", run_a == run_c)


# SAMPLE OUTPUT:
#
# --- TASK 6 ---
# TrainingRun(model='gpt-mini', lr=0.01)
# run_a == run_b: True
# run_a == run_c: False
#
# __str__ is used for a clean, human-readable display.
# __repr__ is normally used for a more detailed/debug representation.


