class TrainingRun:
    run_count = 0
    def __init__(self,model_name,learning_rate):
        if not self.validate(learning_rate):
            raise ValueError("Learning Rate must be in between 0 and 1")
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.status = "Inactive"
        TrainingRun.run_count += 1
    def start(self):
        self.status = "Running"
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

tr1 = TrainingRun("Ollama",0.09)
tr2 = TrainingRun("Codex", 0.12)

config = {"model_name" : "Claude", "learning_rate" :0.05}
tr3 = TrainingRun.from_config(config)

tr1.start()         # Started learning
tr1.summary()       # Ollama with Status Running Learning 0.09
tr2.summary()       # Codex with Status Inactive Learning 0.12
tr3.summary()       # Claude with Status Inactive Learning 0.05
print(TrainingRun.run_count)    # 3