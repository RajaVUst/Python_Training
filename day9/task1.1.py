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

run1=TrainingRun.form_config(config)
run2 = TrainingRun("GPT", 0.01)
run3 = TrainingRun("LSTM", 0.1)

run1.start()
run1.summary()

print(run2.model_name, run2.learning_rate)
print(run3.model_name, run3.learning_rate)

print(TrainingRun.run_count)

# OUTPUT

# BERT training started
# Model:BERT ,Learning rate0.001
# GPT 0.01
# LSTM 0.1
# 3
