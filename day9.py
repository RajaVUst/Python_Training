# Q1
class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"
        self.__api_key = "abc123"

        TrainingRun.run_count += 1

    def start(self):
        self.status = "running"
        print(f"{self.model_name} started")

    def summary(self):
        print(
            f"Model: {self.model_name}, "
            f"LR: {self.learning_rate}, "
            f"Status: {self.status}"
        )

    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )

    @staticmethod
    def validate_learning_rate(lr):
        return 0 < lr < 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ["pending", "running", "done"]:
            raise ValueError("Invalid status")

        self._status = value

    def __str__(self):
        return (
            f"TrainingRun(model='{self.model_name}', "
            f"lr={self.learning_rate})"
        )

    def __eq__(self, other):
        if not isinstance(other, TrainingRun):
            return False

        return (
            self.model_name == other.model_name and
            self.learning_rate == other.learning_rate
        )


run1 = TrainingRun("GPT", 0.01)
run2 = TrainingRun("BERT", 0.001)
run3 = TrainingRun("Llama", 0.005)

print(TrainingRun.run_count)

config = {
    "model_name": "Mistral",
    "learning_rate": 0.02
}

run4 = TrainingRun.from_config(config)
run4.summary()

# Q2
run = TrainingRun("GPT", 0.01)

try:
    run.status = "paused"

except ValueError as e:
    print(e)

try:
    print(run.__api_key)

except AttributeError as e:
    print(e)

print(run._TrainingRun__api_key)

# Q3
class LRSchedulerRun(TrainingRun):

    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule

    def summary(self):
        super().summary()
        print(f"Schedule: {self.schedule}")


scheduler_run = LRSchedulerRun(
    "Transformer",
    0.01,
    [0.01, 0.005, 0.001]
)

scheduler_run.summary()

print(TrainingRun.run_count)

# Q4
class EarlyStoppingRun(TrainingRun):

    def __init__(
        self,
        model_name,
        learning_rate,
        patience
    ):
        super().__init__(model_name, learning_rate)
        self.patience = patience

    def summary(self):
        super().summary()
        print(f"Patience: {self.patience}")


def print_all_summaries(runs):
    for run in runs:
        run.summary()
        print()


runs = [
    TrainingRun("BaseModel", 0.01),
    LRSchedulerRun(
        "SchedulerModel",
        0.005,
        [0.005, 0.002]
    ),
    EarlyStoppingRun(
        "EarlyStopModel",
        0.01,
        5
    )
]

print_all_summaries(runs)

# Q5
class Cleaner:
    def process(self, data):
        return data.strip()


class Tokenizer:
    def process(self, data):
        return data.split()


class Normalizer:
    def process(self, data):
        return [word.lower() for word in data]


def run_pipeline(steps, data):
    for step in steps:
        data = step.process(data)

    return data


steps = [
    Cleaner(),
    Tokenizer(),
    Normalizer()
]

print(run_pipeline(steps, " Hello PYTHON World "))

from abc import ABC, abstractmethod


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


steps2 = [
    CleanerABC(),
    TokenizerABC(),
    NormalizerABC()
]

print(run_pipeline(steps2, " Hello PYTHON World "))

try:
    step = Step()

except TypeError as e:
    print(e)

# Q6
run_a = TrainingRun("GPT", 0.01)
run_b = TrainingRun("GPT", 0.01)
run_c = TrainingRun("BERT", 0.001)

print(run_a)
print(run_a == run_b)
print(run_a == run_c)