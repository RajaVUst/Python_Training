def password_strength(password):

    has_digit = False
    has_uppercase = False

    for ch in password:
        if ch.isdigit():
            has_digit = True

        if ch.isupper():
            has_uppercase = True

    if len(password) >= 8 and has_digit and has_uppercase:
        return "Strong"

    elif len(password) >= 8 and has_digit:
        return "Medium"

    else:
        return "Weak"


print(password_strength("hgyi"))
print(password_strength("python123"))
print(password_strength("Python123"))