class TrainingRun: #for python classes it uses PascalCase
    run_count=0
    
    def __init__(self,model_name,learning_rate):
        self.model_name=model_name
        self.learning_rate=learning_rate
        TrainingRun.run_count+=1
    
    def start(self):
        print(f"{self.model_name} training started")
    
    def summary(self):
        print(f"Model:{self.model_name} ,Learning rate{self.learning_rate}")
        
    @classmethod
    def form_config(cls,config_dict):        
        return cls(
            config_dict["model_name"],
            config_dict["learning_rate"]
        )
        
config={
    "model_name":"BERT",
    "learning_rate":0.001
}



class LRSchedulerRun(TrainingRun):
    
    def __init__(self, model_name, learning_rate,schedule):
        super().__init__(model_name, learning_rate)
        self.schedule=schedule
        
    def summary(self):
        super().summary()
        print(f"schedlue:{self.schedule}")
        

class EarlyStoppingRun(TrainingRun):
    
    def __init__(self, model_name, learning_rate,patience):
        super().__init__(model_name, learning_rate)
        self.patience=patience
        
    def summary(self):
        super().summary()
        print(f"Patinece:{self.patience}")
        

            


def print_all_summaries(runs):
    for run in runs:
        run.summary()

run1 = TrainingRun("BERT", 0.001)

run2 = LRSchedulerRun(
    "GPT",
    0.01,
    [0.01, 0.005, 0.001]
)

run3 = EarlyStoppingRun(
    "LSTM",
    0.1,
    3
)

runs=[run1,run2,run3]

print_all_summaries(runs)


print(f"Run Count:{TrainingRun.run_count}")


# OUTPUT

# Model:BERT ,Learning rate0.001
# Model:GPT ,Learning rate0.01
# schedlue:[0.01, 0.005, 0.001]
# Model:LSTM ,Learning rate0.1
# Patinece:3
# Run Count:3