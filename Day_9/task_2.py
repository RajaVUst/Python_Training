class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.__api_key = "fake_token_12345"
        self._status = "pending"
 
    @property
    def status(self):
        return self._status
 
    @status.setter
    def status(self, value):
        allowed_statuses = ["pending", "running", "done"]
 
        if value not in allowed_statuses:
            raise ValueError(
                "Status must be 'pending', 'running', or 'done'"
            )
 
        self._status = value
 
 
run = TrainingRun("ResNet", 0.01)
 
run.status = "running"
print(run.status)
print(run._TrainingRun__api_key)
 
#Output
'''running
fake_token_12345'''