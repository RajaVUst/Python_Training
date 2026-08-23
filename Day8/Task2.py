class TrainingRun:
    run_count = 0

    def __init__(self, model_name, learning_rate, api_key):
        if not self.validate_learning_rate(learning_rate):
            raise ValueError("Learning rate must be between 0 and 1.")

        self.model_name = model_name
        self.learning_rate = learning_rate

        self.__api_key = api_key
        self._status = "pending"

        TrainingRun.run_count += 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        allowed_statuses = {
            "pending",
            "running",
            "done"
        }

        if new_status not in allowed_statuses:
            raise ValueError(
                "Status must be pending, running, or done."
            )

        self._status = new_status

    def start(self):
        self.status = "running"

    def summary(self):
        return (
            f"Model: {self.model_name}, "
            f"Learning rate: {self.learning_rate}, "
            f"Status: {self.status}"
        )

    @staticmethod
    def validate_learning_rate(learning_rate):
        return 0 < learning_rate < 1


run = TrainingRun(
    "gpt-mini",
    0.01,
    "fake-secret-token"
)

print("Initial status:", run.status)

run.status = "running"
print("Updated status:", run.status)


try:
    run.status = "paused"
except ValueError as error:
    print("Invalid status error:", error)


try:
    print(run.__api_key)
except AttributeError as error:
    print("Direct private access failed:", error)


print(
    "Access through name mangling:",
    run._TrainingRun__api_key
)

# Java's private keyword is enforced by the compiler.
# Python relies on naming conventions and name mangling, trusting developers
# not to access internal attributes unless there is a valid reason.


#output
'''
Initial status: pending
Updated status: running
Invalid status error: Status must be pending, running, or done.
Direct private access failed: 'TrainingRun' object has no attribute '__api_key'
Access through name mangling: fake-secret-token

'''