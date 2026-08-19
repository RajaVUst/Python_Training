class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")

    return score


scores = [85, 105, 72, -5, 95]

for score in scores:
    try:
        print(f"{score}: Valid")

        validate_score(score)

    except InvalidScoreError as e:
        print(f"{score}: {e}")

# output:
# 85: Valid
# 105: Valid
# 105: Score must be between 0 and 100
# 72: Valid
# -5: Valid
# -5: Score must be between 0 and 100
# 95: Valid