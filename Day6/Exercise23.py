
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    print(check_age(25))
except ValueError as e:
    print("Error:", e)


try:
    print(check_age(-5))
except ValueError as e:
    print("Error:", e)

#output
# 25
# Error: Age cannot be negative