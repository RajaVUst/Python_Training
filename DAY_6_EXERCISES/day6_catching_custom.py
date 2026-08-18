class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")
    return score


scores = [95, -5, 100, 120, 78]

for score in scores:
    try:
        valid_score = validate_score(score)
        print(f"Valid score: {valid_score}")

    except InvalidScoreError as e:
        print(f"Invalid score {score}: {e}")

"""
Output->
Valid score: 95
Invalid score -5: Score must be between 0 and 100
Valid score: 100
Invalid score 120: Score must be between 0 and 100
Valid score: 78
"""