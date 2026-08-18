class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(
            "Score must be between 0 and 100."
        )
    return score


scores = [95, -10, 75, 120, 88]

for score in scores:
    try:
        valid_score = validate_score(score)
        print(f"{valid_score} is valid")

    except InvalidScoreError as e:
        print(f"{score} is invalid: {e}")

"""
95 is valid
-10 is invalid: Score must be between 0 and 100.
75 is valid
120 is invalid: Score must be between 0 and 100.
88 is valid
"""