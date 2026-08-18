# Exercise 23 - Raise a built-in exception
def check_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(f"Caught error: {e}")
# Output:
# 25
# Caught error: Age cannot be negative: -5

# Exercise 24 - Define a custom exception
class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError(f"Score {score} is out of range (0-100)")
    return score

print(validate_score(88))
# Output: 88

# Exercise 25 - Catch your custom exception
test_scores = [88, 150, -10, 76, 205]
for score in test_scores:
    try:
        print(f"{validate_score(score)} is valid.")
    except InvalidScoreError as e:
        print(f"Rejected: {e}")
# Output:
# 88 is valid.
# Rejected: Score 150 is out of range (0-100)
# Rejected: Score -10 is out of range (0-100)
# 76 is valid.
# Rejected: Score 205 is out of range (0-100)