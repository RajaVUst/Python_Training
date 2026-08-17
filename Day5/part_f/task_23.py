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
    "python",
    "hello123",
    "Python2026",
    "abcdefghij5"
]

print(password_report(passwords))


# {'weak': ['abc'], 'medium': ['python', 'hello123'], 'strong': ['Python2026', 'abcdefghij5']}
