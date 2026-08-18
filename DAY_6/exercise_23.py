def check_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}.")
    return age

# Valid value
try:
    print(check_age(25))
except ValueError as e:
    print("Error:", e)

# Invalid value
try:
    print(check_age(-3))
except ValueError as e:
    print("Error:", e)
