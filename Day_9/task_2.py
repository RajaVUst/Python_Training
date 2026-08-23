class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name          
        self.learning_rate = learning_rate 

        self._status = "pending"             
        self.__api_key = "fake_token_123"  

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = {"pending", "running", "done"}

        if value not in allowed:
            raise ValueError(
                "Status must be 'pending', 'running', or 'done'"
            )

        self._status = value


run = TrainingRun("ResNet50", 0.01)

run.status = "running"
print(run.status)

try:
    run.status = "paused"
except ValueError as e:
    print("Error:", e)

try:
    print(run.__api_key)
except AttributeError as e:
    print("AttributeError:", e)

print(run._TrainingRun__api_key)

# In Java, the private keyword is enforced by the compiler, so code outside the class cannot directly access private fields. 
# In Python,private attributes are implemented through name mangling, not strict access control. 
# Python trusts developers to follow conventions and avoid accessing internal attributes unless they intentionally choose to do so.

