def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


try:
    print(check_age(25))
    print(check_age(-5))

except ValueError as e:
    print("Error:", e)


# 25
# Error: Age cannot be negative.