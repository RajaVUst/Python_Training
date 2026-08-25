class TrainingRun:
    def __init__(self,model_name,learning_rate):
        self.model_name=model_name
        self.learning_rate=learning_rate
        self.__api_key="fake-token-123"
        self._status="pending"
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,value):
        if value in ['pending','running','done']:
            self._status=value
        else:
            raise ValueError("Invalid Status")
        
run1=TrainingRun("Bert",0.001)
print(run1.status)

run1.status="running"

print(run1.status)


try:
    run1.status = "paused"
except ValueError as e: 
    print(e)


print(run1._TrainingRun__api_key)
try:
    print(run1.__api_key)
except AttributeError:
    print("Api Key cannot be accessed directly")
# OUTPUT

# pending
# running
# Invalid Status
# fake-token-123
# Api Key cannot be accessed directly