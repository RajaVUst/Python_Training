class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"                     
        self.__api_key = f"key-{model_name}-secret"    
        TrainingRun.run_count += 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = ("pending", "running", "done")
        if value not in allowed:
            raise ValueError(f"status must be one of {allowed}")
        self._status = value


r1 = TrainingRun("gpt-mini", 0.01)
r1.status = "running"
print(r1.status)

try:
    r1.status = "paused"
except ValueError as e:
    print(f"ValueError: {e}")

try:
    print(r1.__api_key)
except AttributeError as e:
    print(f"AttributeError: {e}")

print(r1._TrainingRun__api_key)  

# Output:
# running
# ValueError: status must be one of ('pending', 'running', 'done')
# AttributeError: 'TrainingRun' object has no attribute '__api_key'
# key-gpt-mini-secret