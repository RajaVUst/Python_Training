def password_report(passwords):
    result = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for password in passwords:
        has_digit = any(char.isdigit() for char in password)

        if len(password) >= 10 and has_digit:
            result["strong"].append(password)
        elif len(password) >= 6:
            result["medium"].append(password)
        else:
            result["weak"].append(password)

    return result


# Test with sample passwords
passwords = [
    "abc",
    "hello",
    "python",
    "python123",
    "hello12345",
    "StrongPass123"
]

print(password_report(passwords))
#output
"""
{'weak': ['abc', 'hello'], 'medium': ['python', 'python123'], 'strong': ['hello12345', 'StrongPass123']}"""