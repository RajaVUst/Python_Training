from task2 import TrainingRun

class LRSchedulerRun(TrainingRun):
    def __init__(self,model_name,learning_rate,schedule):
        super().__init__(model_name,learning_rate)
        self.schedule = schedule
        
    def summary(self):
        super().summary()
        print("Current scheduled Learning rate",self.schedule[0])

run = LRSchedulerRun("grok",0.06, [0.005,0.9,0.09])
run.summary()       # grok with Status pending Learning 0.06
                    # Current scheduled Learning rate 0.005
print(TrainingRun.run_count)    # 2