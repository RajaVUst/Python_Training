def password_strength(password):
    has_digit = False
    has_upper = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True

    if len(password) >= 8 and has_digit and has_upper:
        return "Strong"
    elif len(password) >= 6 and (has_digit or has_upper):
        return "Medium"
    else:
        return "Weak"

print(password_strength("hello world"))
print(password_strength("helloworld12"))
print(password_strength("Helloworld123"))

# output
# Weak
# Medium
# Strong
