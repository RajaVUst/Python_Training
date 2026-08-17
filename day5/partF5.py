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


passwords = ["abc", "python", "Python12345", "hello1", "securepass9"]

print(password_report(passwords))

# OUTPUT

# {'weak': ['abc'], 
#  'medium': ['python', 'hello1'],
#  'strong': ['Python12345', 'securepass9']}