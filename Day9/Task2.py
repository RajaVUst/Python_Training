class TrainingRun:
    run_count = 0
 
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate
 
        self.__api_key = "fhdkjheuriwerncnwor"
 
        self._status = "pending"
 
        TrainingRun.run_count += 1
 
    @property
    def status(self):
        return self._status
 
    @status.setter
    def status(self, value):
        value = value.lower()
 
        if value not in ["pending", "running", "done"]:
            raise ValueError(
                "Status must be 'pending', 'running', or 'done'"
            )
 
        self._status = value
 
    def training_start(self):
        self.status = "running"
 
    def training_summary(self):
        print(f"Model Name: {self.model_name}")
        print(f"Learning Rate: {self.learning_rate}")
        print(f"Status: {self.status}")
 
        return {
            "Model Name": self.model_name,
            "Learning Rate": self.learning_rate,
            "Status": self.status
        }
 
    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )
 
 
run1 = TrainingRun("ResNet50", 4)
run2 = TrainingRun("BERT", 2)
run3 = TrainingRun.from_config(
    {"model_name": "GPT", "learning_rate": 1}
)
 
run1.training_start()
 
print(run1.training_summary())
print(run2.training_summary())
print(run3.training_summary())
 
print("Total runs:", TrainingRun.run_count)
 
try:
    print(run1.__api_key)
except AttributeError as e:
    print("AttributeError:", e)
 
print(run1._TrainingRun__api_key)
 
try:
    run1.status = "paused"
except ValueError as e:
    print("ValueError:", e)
 
# Output:
"""
Model Name: ResNet50
Learning Rate: 4
Status: running
{'Model Name': 'ResNet50', 'Learning Rate': 4, 'Status': 'running'}
Model Name: BERT
Learning Rate: 2
Status: pending
{'Model Name': 'BERT', 'Learning Rate': 2, 'Status': 'pending'}
Model Name: GPT
Learning Rate: 1
Status: pending
{'Model Name': 'GPT', 'Learning Rate': 1, 'Status': 'pending'}
Total runs: 3
AttributeError: 'TrainingRun' object has no attribute '__api_key'
fhdkjheuriwerncnwor
ValueError: Status must be 'pending', 'running', or 'done'
"""
 