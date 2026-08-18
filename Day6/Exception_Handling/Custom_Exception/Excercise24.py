# Define a custom exception

class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")
    return score

# Output:
# Just define the exception. So that no any particular output.