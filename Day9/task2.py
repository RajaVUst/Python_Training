class TrainingRun:
    run_count = 0
    def __init__(self,model_name,learning_rate):
        if not self.validate(learning_rate):
            raise ValueError("Learning Rate must be in between 0 and 1")
        self.model_name = model_name
        self.learning_rate = learning_rate
        self._status = "pending"
        self.__api_key = "hfiwu332fji23rh231"
        TrainingRun.run_count += 1
    def start(self):
        self._status = "running"
        print("Started learning")
    def summary(self):
        print(f"{self.model_name} with Status {self.status} Learning {self.learning_rate}")
    @classmethod
    def from_config(cls,config_dict):
        return cls(config_dict["model_name"],
                config_dict["learning_rate"])
    @staticmethod
    def validate(lr):
        return 0 < lr < 1
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,val):
        if val not in ('pending','running','done'):
            raise ValueError("Invalid Status")
        self._status = val

tr = TrainingRun("Gemini",0.02)
tr.summary()        # Gemini with Status pending Learning 0.02
tr.start()          # Started learning
print(tr.status)    # running
print(tr._TrainingRun__api_key)   # name-mangling hfiwu332fji23rh231
tr.status = "done"
#print(tr.__api_key)     # AttributeError: 'TrainingRun' object has no attribute '__api_key'
#tr.status = "pause"     # ValueError: Invalid Status