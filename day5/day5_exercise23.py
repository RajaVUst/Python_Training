def password_report(passwords):
    report = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for pw in passwords:
        has_digit = any(ch.isdigit() for ch in pw)

        if len(pw) >= 10 and has_digit:
            report["strong"].append(pw)
        elif len(pw) >= 6:
            report["medium"].append(pw)
        else:
            report["weak"].append(pw)

    return report


passwords = [
    "abc",
    "python",
    "pass12",
    "welcome123",
    "StrongPass2024"
]

print(password_report(passwords))

"""
OUTPUT:
{'weak': ['abc'], 'medium': ['python', 'pass12'], 'strong': ['welcome123', 'StrongPass2024']}
"""