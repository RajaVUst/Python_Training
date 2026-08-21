
class TrainingRun:

    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

        self.__api_key = "FAKE-API-12345"

        self._status = "pending"

        TrainingRun.run_count += 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        if value not in ["pending", "running", "done"]:
            raise ValueError("Invalid status")

        self._status = value


run = TrainingRun("GPT-Mini", 0.01)

print("Initial Status:", run.status)

run.status = "running"

print("Updated Status:", run.status)

try:
    run.status = "paused"
except ValueError as e:
    print("Error:", e)

try:
    print(run.__api_key)
except AttributeError:
    print("Cannot access __api_key directly")

print("API Key:", run._TrainingRun__api_key)


# OUTPUT:
# Initial Status: pending
# Updated Status: running
# Error: Invalid status
# Cannot access __api_key directly
# API Key: FAKE-API-12345