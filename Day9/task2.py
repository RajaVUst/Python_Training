#Apply Python's encapsulation conventions (public / _protected / __private)

class TrainingRun:
    run_count = 0
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.__api_key = "ABC123"
        self._status = "pending"
        TrainingRun.run_count += 1

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        if value == "pending" or value == "running" or value == "done":
            self._status = value
        else:
            raise ValueError("Invalid status")

    def summary(self):
        print("Model:", self.model_name)
        print("Learning Rate:", self.learning_rate)
        print("Status:", self.status)


run = TrainingRun("gpt-mini", 0.01)
print(run.status)
run.status = "running"
print(run.status)


# Output:
# Testing invalid value - ValueError: Invalid status
# Private variable - print(run.__api_key)
# name mangling- ABC123