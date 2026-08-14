def password_strength(password):
    has_uppercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        if char.isdigit():
            has_digit = True

    if len(password) >= 8 and has_uppercase and has_digit:
        return "Strong"
    elif len(password) >= 6 and (has_uppercase or has_digit):
        return "Medium"
    else:
        return "Weak"


print(f"'password' -> {password_strength('password')}")
print(f"'Python7' -> {password_strength('Python7')}")
print(f"'SecurePass123' -> {password_strength('SecurePass123')}")

#Output:
"""
'password' -> Weak
'Python7' -> Medium
'SecurePass123' -> Strong
"""