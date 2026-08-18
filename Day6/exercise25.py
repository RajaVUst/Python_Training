# Day 6 - Exercise 25
class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(
            f"Score {score} must be between 0 and 100."
        )

    return score


test_scores = [75, -10, 100, 120, 45]

for score in test_scores:
    try:
        valid_score = validate_score(score)
        print(f"{valid_score} is valid.")

    except InvalidScoreError as error:
        print("Error:", error)

#output
'''
75 is valid.
Error: Score -10 must be between 0 and 100.
100 is valid.
Error: Score 120 must be between 0 and 100.
45 is valid.
'''
