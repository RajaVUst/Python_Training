# Raise a built-in exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    age = check_age(-5)
    print(age)

except ValueError as e:
    print(e)

# Output:
# Age cannot be negative