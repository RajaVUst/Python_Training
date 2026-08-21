class TrainingRun:
    run_count=0
    def __init__(self, model_name, learning_rate):
        self.model_name=model_name
        self.learning_rate=learning_rate
        self.status=False
        TrainingRun.run_count += 1

    def training_start(self):
        self.status=True
        
    def training_summary(self):
        print(f"Model Name: {self.model_name}")
        print(f"Learning Rate: {self.learning_rate}")
        print(f"Status: {self.status}") 

        return{
            f"Model Name: {self.model_name}",
            f"Learning Rate: {self.learning_rate}", 
            f"Status: {self.status}"
        }

    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )

run1 = TrainingRun("ResNet50", 4)
run2 = TrainingRun("BERT", 2)
run3 = TrainingRun.from_config({"model_name": "GPT","learning_rate": 1})

run1.training_start()

print(run1.training_summary())
print(run2.training_summary())
print(run3.training_summary())

print("Total runs:", TrainingRun.run_count)

# Output:
"""
Model Name: ResNet50
Learning Rate: 4
Status: True
{'Learning Rate: 4', 'Status: True', 'Model Name: ResNet50'}
Model Name: BERT
Learning Rate: 2
Status: False
{'Learning Rate: 2', 'Model Name: BERT', 'Status: False'}
Model Name: GPT
Learning Rate: 1
Status: False
{'Model Name: GPT', 'Status: False', 'Learning Rate: 1'}
Total runs: 3
"""