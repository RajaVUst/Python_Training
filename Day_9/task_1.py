class TrainingRun:
    run_count = 0
 
    def __init__(self, model_name, learning_rate):
 
        if not TrainingRun.validate_learning_rate(learning_rate):
            raise ValueError("Learning rate must be between 0 and 1")
 
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "Not Started"
        TrainingRun.run_count+=1
 
    def start(self):
        self.status = "Running"
        print(f"Training started for {self.model_name}")
 
    def summary(self):
        return (
            f"Model: {self.model_name}, "
            f"Learning Rate: {self.learning_rate}, "
            f"Status: {self.status}"
            )
 
    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )
 
    @staticmethod
    def validate_learning_rate(lr):
        return 0 < lr < 1
 
config = {
"model_name": "GPT",
"learning_rate": 0.1
}
run1 = TrainingRun.from_config(config)
 
run1.start()
print(run1.summary())

#Output
 
'''Training started for GPT
Model: GPT, Learning Rate: 0.1, Status: Running'''