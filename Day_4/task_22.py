def password_strength(password):
    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    if len(password) >= 10 and has_digit and has_upper:
        return "Strong"
    elif len(password) >= 8 and (has_digit or has_upper):
        return "Medium"
    else:
        return "Weak"

print(password_strength("hello"))
print(password_strength("Hello123"))
print(password_strength("HelloWorld123"))

# output:
# Weak
# Medium
# Strong