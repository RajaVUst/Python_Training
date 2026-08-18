# Exercise 23: Raise a built-in exception
def check_age(age):
    if age < 0:
        raise ValueError("age can't be negative")
    return age
try:
    check_age(-8)
except ValueError as e:
    print(e)        # age can't be negative

# Exercise 24: Define a custom exception
class InvalidScoreError(Exception):
    pass
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")
    return score

try:
    print(validate_score(85))
    print(validate_score(120))
except InvalidScoreError as e:
    print(e)

"""
Output->
85
Score must be between 0 and 100
"""
# Exercise 25: Catch your custom exception
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