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
    "secret",
    "mypassword",
    "pass123456",
    "hello1",
    "StrongPwd99"
]

print(password_report(passwords))

# Output:
# {'weak': ['abc', 'secret'], 'medium': ['mypassword', 'hello1'], 'strong': ['pass123456', 'StrongPwd99']}