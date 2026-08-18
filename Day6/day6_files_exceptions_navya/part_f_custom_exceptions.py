# Exercise 23 - Raise a built-in exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

print(check_age(25))

try:
    check_age(-5)
except ValueError as e:
    print(e)
# Output:
# 25
# Age cannot be negative


# Exercise 24 - Define a custom exception
class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")
    return score

print(validate_score(85))
# Output: 85


# Exercise 25 - Catch your custom exception
test_scores = [85, 105, -10, 60, 200]

for score in test_scores:
    try:
        print(validate_score(score))
    except InvalidScoreError as e:
        print(f"Skipped {score}: {e}")
# Output:
# 85
# Skipped 105: Score must be between 0 and 100
# Skipped -10: Score must be between 0 and 100
# 60
# Skipped 200: Score must be between 0 and 100