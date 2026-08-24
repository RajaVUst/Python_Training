# DESIGN A CLASS
 
class TrainingRun:
    run_count = 0
 
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        TrainingRun.run_count += 1
 
    @classmethod
    def from_config(cls, config):
        return cls(config["model_name"], config["learning_rate"])
 
    def start(self):
        print(f"Training started for {self.model_name}")
 
    def summary(self):
        return f"Model: {self.model_name}, LR: {self.learning_rate}"
 
 
run1 = TrainingRun("GPT-Mini", 0.01)
run2 = TrainingRun("BERT", 0.001)
run3 = TrainingRun.from_config(
    {"model_name": "Llama", "learning_rate": 0.005}
)
 
print(run1.summary())
print(run2.summary())
print(run3.summary())
print("Run Count:", TrainingRun.run_count)
 
# Output:
# Model: GPT-Mini, LR: 0.01
# Model: BERT, LR: 0.001
# Model: Llama, LR: 0.005
# Run Count: 3
 
 # ENCAPSULATION
 
class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.__api_key = "secret_token"
        self._status = "pending"
 
    @property
    def status(self):
        return self._status
 
    @status.setter
    def status(self, value):
        allowed = ["pending", "running", "done"]
 
        if value not in allowed:
            raise ValueError("Invalid status")
 
        self._status = value
 
 
run = TrainingRun("GPT-Mini", 0.01)
 
print("Initial Status:", run.status)
 
run.status = "running"
print("Updated Status:", run.status)
 
try:
    run.status = "paused"
except ValueError as e:
    print(e)
 
try:
    print(run.__api_key)
except AttributeError as e:
    print(e)
 
print(run._TrainingRun__api_key)
 
# Output:
# Initial Status: pending
# Updated Status: running
# Invalid status
# 'TrainingRun' object has no attribute '__api_key'
# secret_token
 
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
 
# POLYMORPHISM
 
class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
 
    def summary(self):
        return f"Model: {self.model_name}, LR: {self.learning_rate}"
 
 
class LRSchedulerRun(TrainingRun):
    def __init__(self, model_name, learning_rate, schedule):
        super().__init__(model_name, learning_rate)
        self.schedule = schedule
 
    def summary(self):
        return f"{super().summary()}, Schedule: {self.schedule}"
 
 
class EarlyStoppingRun(TrainingRun):
    def __init__(self, model_name, learning_rate, patience):
        super().__init__(model_name, learning_rate)
        self.patience = patience
 
    def summary(self):
        return f"{super().summary()}, Patience: {self.patience}"
 
 
def print_all_summaries(runs):
    for run in runs:
        print(run.summary())
 
 
runs = [
    TrainingRun("GPT-Mini", 0.01),
    LRSchedulerRun("GPT-Scheduler", 0.01, [0.01, 0.005]),
    EarlyStoppingRun("GPT-Early", 0.01, 5)
]
 
print_all_summaries(runs)
 
# Output:
# Model: GPT-Mini, LR: 0.01
# Model: GPT-Scheduler, LR: 0.01, Schedule: [0.01, 0.005]
# Model: GPT-Early, LR: 0.01, Patience: 5
 
# DUCK TYPING & INTERFACES
 
from abc import ABC, abstractmethod
 
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
 
print(run_pipeline(steps, " HELLO WORLD PYTHON "))
 
 
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
 
 
steps_abc = [
    CleanerABC(),
    TokenizerABC(),
    NormalizerABC()
]
 
print(run_pipeline(steps_abc, " HELLO WORLD PYTHON "))
 
try:
    step = Step()
except TypeError as e:
    print(e)
 
# Output:
# ['hello', 'world', 'python']
# ['hello', 'world', 'python']
# Can't instantiate abstract class Step with abstract method process
 
# DUNER METHODS
 
class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
 
    def __str__(self):
        return f"TrainingRun(model='{self.model_name}', lr={self.learning_rate})"
 
    def __eq__(self, other):
        return (
            self.model_name == other.model_name
            and self.learning_rate == other.learning_rate
        )
 
    def __repr__(self):
        return f"TrainingRun('{self.model_name}', {self.learning_rate})"
 
 
run1 = TrainingRun("GPT", 0.01)
run2 = TrainingRun("GPT", 0.01)
run3 = TrainingRun("BERT", 0.01)
 
print(run1)
print(run1 == run2)
print(run1 == run3)
print(repr(run1))
 
# Output:
# TrainingRun(model='GPT', lr=0.01)
# True
# False
# TrainingRun('GPT', 0.01)
 