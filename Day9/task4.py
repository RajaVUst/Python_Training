from task3 import TrainingRun, LRSchedulerRun
class EarlyStoppingRun(TrainingRun):
    def __init__(self,model_name,learning_rate,patience):
        super().__init__(model_name,learning_rate)
        self.patience = patience
    def summary(self):
        super().summary()
        print(f"Patience {self.patience} epochs")

def print_all_summaries(runs):
    for run in runs:
        run.summary()

run1 = TrainingRun("gpt-mini",0.008)
run2 = LRSchedulerRun("gpt-4.0",0.004,[0.01,0.8,0.04])
run3 = EarlyStoppingRun("opus",0.03,5)

runs = [run1, run2, run3]
print_all_summaries(runs)

# Output --> 
# gpt-mini with Status pending Learning 0.008
# gpt-4.0 with Status pending Learning 0.004
# Current scheduled Learning rate 0.01
# opus with Status pending Learning 0.03
# Patience 5 epochs