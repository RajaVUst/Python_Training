class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return score


for test_score in (95, -5, 70, 120, 0):
    try:
        print("Valid score:", validate_score(test_score))
    except InvalidScoreError as error:
        print(f"Invalid score {test_score}: {error}")

# OUTPUT

# Valid score: 95
# Invalid score -5: Score must be between 0 and 100.
# Valid score: 70
# Invalid score 120: Score must be between 0 and 100.
# Valid score: 0
