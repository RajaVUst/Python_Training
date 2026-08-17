def password_report(passwords):
    result = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for pw in passwords:
        if len(pw) >= 10 and any(ch.isdigit() for ch in pw):
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
    "Python12345",
    "welcome",
    "test1"
]
print(password_report(passwords))

# output
# {'weak': ['abc', 'test1'], 'medium': ['python', 'hello123', 'welcome'], 'strong': ['Python12345']