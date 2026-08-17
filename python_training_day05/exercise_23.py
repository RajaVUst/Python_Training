def password_report(passwords):
    result = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for password in passwords:
        has_digit = any(ch.isdigit() for ch in password)

        if len(password) >= 10 and has_digit:
            result["strong"].append(password)
        elif len(password) >= 6:
            result["medium"].append(password)
        else:
            result["weak"].append(password)

    return result


passwords = [
    "abc",
    "python",
    "hello12",
    "python1234",
    "securePass9",
    "test"
]

print(password_report(passwords))



#output:
'''{'weak': ['abc', 'test'], 'medium': ['python', 'hello12'],
 'strong': ['python1234', 'securePass9']}'''