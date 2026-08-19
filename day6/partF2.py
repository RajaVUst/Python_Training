class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return score


print(validate_score(85))

# OUTPUT

# 85
