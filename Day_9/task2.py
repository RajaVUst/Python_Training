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