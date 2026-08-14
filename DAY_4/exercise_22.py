def password_strength(password):
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    long_enough = len(password) >= 8

    if long_enough and has_upper and has_digit:
        return "Strong"
    elif long_enough or (has_upper and has_digit):
        return "Medium"
    else:
        return "Weak"

print(password_strength("abc"))           # Weak
print(password_strength("Abcdefgh"))      # Medium
print(password_strength("Secure123"))     # Strong
