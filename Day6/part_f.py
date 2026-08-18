# Exercise 23: Raise a built-in exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age
try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(e)
# Output:
# 25
# Age cannot be negative.


# Exercise 24: Define a custom exception
class InvalidScoreError(Exception):
    pass
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return score
try:
    print(validate_score(85))
    print(validate_score(120))
except InvalidScoreError as e:
    print(e)
# Output:
# 85
# Score must be between 0 and 100.


# Exercise 25: Catch your custom exception
class InvalidScoreError(Exception):
    pass
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return score
scores = [85, 120, 75, -10, 95]
for score in scores:
    try:
        print("Valid Score:", validate_score(score))

    except InvalidScoreError as e:
        print(f"Invalid Score ({score}):", e)
# Output:
# Valid Score: 85
# Invalid Score (120): Score must be between 0 and 100.
# Valid Score: 75
# Invalid Score (-10): Score must be between 0 and 100.
# Valid Score: 95