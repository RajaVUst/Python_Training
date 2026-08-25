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
        
    def __str__(self):
        return f"Training model:{self.model_name},learning Rate:{self.learning_rate}"
        
    def __eq__(self, other):
        return(
            self.model_name==other.model_name
            and self.learning_rate==other.learning_rate
        )
config={
    "model_name":"BERT",
    "learning_rate":0.001
}

run1=TrainingRun.form_config(config)

run1.start()
run1.summary()

print(f"Testing Str method:{run1}")

# Testing the equ dunder method 


run4=TrainingRun("BERT",0.001)

print(f"Checking equ:{run1==run4}")

print(TrainingRun.run_count)
# OUTPUT

# Model:BERT ,Learning rate0.001
# Testing Str method:Training model:BERT,learning Rate:0.001
# Checking equ:True
# 2