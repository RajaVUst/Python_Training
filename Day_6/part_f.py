# =========================
# Exercise 23: Raise a Built-in Exception
# =========================

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age


print("Exercise 23")

try:
    print("Valid age:", check_age(25))
    print("Invalid age:", check_age(-5))

except ValueError as e:
    print("Error:", e)

print()


# =========================
# Exercise 24: Define a Custom Exception
# =========================

class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(
            f"Score {score} is invalid. Must be between 0 and 100."
        )

    return score


print("Exercise 24")

try:
    print("Valid score:", validate_score(85))
    print("Invalid score:", validate_score(120))

except InvalidScoreError as e:
    print("Error:", e)

print()


# =========================
# Exercise 25: Catch Your Custom Exception
# =========================

print("Exercise 25")

test_scores = [95, -10, 75, 105, 50]

for score in test_scores:
    try:
        validated = validate_score(score)
        print(f"{validated} -> Valid")

    except InvalidScoreError as e:
        print(f"{score} -> Error: {e}")

#output
'''Exercise 23
Valid age: 25
Error: Age cannot be negative.

Exercise 24
Valid score: 85
Error: Score 120 is invalid. Must be between 0 and 100.

Exercise 25
95 -> Valid
-10 -> Error: Score -10 is invalid. Must be between 0 and 100.
75 -> Valid
105 -> Error: Score 105 is invalid. Must be between 0 and 100.
50 -> Valid'''