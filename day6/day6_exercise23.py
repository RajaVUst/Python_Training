def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age


# Valid value
try:
    print(check_age(25))
except ValueError as e:
    print("Error:", e)

# Invalid value
try:
    print(check_age(-5))
except ValueError as e:
    print("Error:", e)

"""
OUTPUT:
25
Error: Age cannot be negative.
"""