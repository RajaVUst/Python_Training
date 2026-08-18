class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if not (0 <= score <= 100):
        raise InvalidScoreError(f"{score} is not between 0 and 100")
    return score

test_scores = [85, -10, 101, 42, 0]
for s in test_scores:
    try:
        print(validate_score(s))
    except InvalidScoreError as e:
        print("Invalid:", e)
#output
# 85
# Invalid: -10 is not between 0 and 100
# Invalid: 101 is not between 0 and 100
# 42
# 0