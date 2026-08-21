class TrainingRun:

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

        self._status = "pending"

        self.__api_key = "FAKE_API_KEY_123"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        if value not in ["pending", "running", "done"]:
            raise ValueError("Status must be pending, running, or done")

        self._status = value


run = TrainingRun("GPT-Model", 0.01)

print("Initial status:", run.status)

run.status = "running"
print("Updated status:", run.status)

run.status = "done"
print("Final status:", run.status)


try:
    run.status = "paused"
except ValueError as e:
    print("Error:", e)


try:
    print(run.__api_key)
except AttributeError as e:
    print("Error:", e)


print("API Key:", run._TrainingRun__api_key)



# Initial status: pending
# Updated status: running
# Final status: done
# Error: Status must be pending, running, or done
# Error: 'TrainingRun' object has no attribute '__api_key'
# API Key: FAKE_API_KEY_123