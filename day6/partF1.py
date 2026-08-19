def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age


for test_age in (25, -3):
    try:
        print("Valid age:", check_age(test_age))
    except ValueError as error:
        print("Error:", error)

# OUTPUT

# Valid age: 25
# Error: Age cannot be negative.
