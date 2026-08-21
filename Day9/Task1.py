class TrainingRun:
    run_count=0
    def __init__(self,model_name,learning_rate):
        if not self.validate_learning_rate(learning_rate):
            raise ValueError("Learning must be between 0 & 1")
        self.model_name=model_name
        self.learning_rate=learning_rate
        self.status="Not Started"
        TrainingRun.run_count+=1
    def start(self):
        self.status="running"
        print(f"{self.model_name} training Started")
    def summary(self):
        return(
            f"Model:{self.model_name},"
            f"Learning Rate:{self.learning_rate}"
            f"status:{self.status}"
        )
    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )
    @staticmethod
    def validate_learning_rate(learning_rate):
        return 0<learning_rate<1
run1 = TrainingRun("ResNet", 0.01)
run2 = TrainingRun("BERT", 0.001)
run3 = TrainingRun("XGBoost", 0.05)

print(TrainingRun.run_count)
run1.start()
print(run2.summary())

#output
"""
3
ResNet training Started
Model:BERT,Learning Rate:0.001status:Not Started
"""
