def password_strength(password):
    has_digit = False
    has_upper = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True

    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and has_digit and has_upper:
        return "Strong"
    else:
        return "Medium"

passwords = ["abc", "python123", "Python123"]

for password in passwords:
    print(f"{password} -> {password_strength(password)}")



#output:
'''abc -> Weak
python123 -> Medium
Python123 -> Strong'''