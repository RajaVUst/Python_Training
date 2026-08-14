def password_strength(password):
    has_digit = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and has_digit and has_upper:
        return "Strong"
    else:
        return "Medium"
print(password_strength("abc"))
print(password_strength("python12"))
print(password_strength("Python123"))

"""
output
Weak
Medium
Strong
"""