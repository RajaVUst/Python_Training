def password_strength(password):
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)

    if len(password) >= 8 and has_digit and has_upper:
        return "Strong"
    elif len(password) >= 6 and (has_digit or has_upper):
        return "Medium"
    else:
        return "Weak"

print(f"pranav -> {password_strength('pranav')}")
print(f"pranav123 -> {password_strength('pranav123')}")
print(f"Pranav123 -> {password_strength('Pranav123')}")

"""
Output ->
pranav -> Weak
pranav123 -> Medium
Pranav123 -> Strong
"""