def password_report(passwords):
    result = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for pw in passwords:
        has_digit = any(ch.isdigit() for ch in pw)

        if len(pw) >= 10 and has_digit:
            result["strong"].append(pw)
        elif len(pw) >= 6:
            result["medium"].append(pw)
        else:
            result["weak"].append(pw)

    return result


passwords = [
    "abc",
    "hello1",
    "python",
    "password123",
    "Secure2026",
    "test"
]

print(password_report(passwords))

# output:
# {'weak': ['abc', 'test'], 'medium': ['hello1', 'python'], 'strong': ['password123', 'Secure2026']}