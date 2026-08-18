class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")

    return score


scores = [85, 105, 72, -10, 95]

for score in scores:
    try:
        validate_score(score)
        print(score, "is valid.")

    except InvalidScoreError as e:
        print(score, "is invalid:", e)


# 85 is valid.
# 105 is invalid: Score must be between 0 and 100.
# 72 is valid.
# -10 is invalid: Score must be between 0 and 100.
# 95 is valid.