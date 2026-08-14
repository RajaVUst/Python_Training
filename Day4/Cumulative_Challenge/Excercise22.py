# Password_Strength

def password_strength(password):

    has_digit = False
    has_uppercase = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_uppercase = True

    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and has_digit and has_uppercase:
        return "Strong"
    else:
        return "Medium"

print(password_strength("abc"))
print(password_strength("password"))
print(password_strength("Logesh2322"))

# Output:
# Weak
# Medium
# Strong