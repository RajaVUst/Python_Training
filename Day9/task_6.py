class TrainingRun:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

    def __str__(self):
        return f"TrainingRun(model='{self.model_name}', lr={self.learning_rate})"

    def __eq__(self, other):
        if not isinstance(other, TrainingRun):
            return NotImplemented

        return (
            self.model_name == other.model_name
            and self.learning_rate == other.learning_rate
        )

    # Stretch goal:
    def __repr__(self):
        # __str__ is mainly for a clean, human-readable representation.
        # __repr__ is intended to provide a more detailed/developer-friendly
        # representation, especially while debugging.
        return (
            f"TrainingRun(model_name='{self.model_name}', "
            f"learning_rate={self.learning_rate})"
        )


# Create two separate objects with the same values
run1 = TrainingRun("gpt-mini", 0.01)
run2 = TrainingRun("gpt-mini", 0.01)

# __str__ is called automatically by print()
print(run1)

# __eq__ is called automatically by ==
print(run1 == run2)

# Different values
run3 = TrainingRun("gpt-large", 0.01)

print(run1 == run3)

# __repr__ can be called explicitly
print(repr(run1))




# TrainingRun(model='gpt-mini', lr=0.01)
# True
# False
# TrainingRun(model_name='gpt-mini', learning_rate=0.01)