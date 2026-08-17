# Password Strength Report 

def password_report(passwords):
    result = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for password in passwords:
        has_digit = False
        for char in password:
            if char.isdigit():
                has_digit = True

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
    "mypassword",
    "python12345",
    "test"
]
print(password_report(passwords))


# Output:
# {'weak': ['abc', 'test'], 'medium': ['python', 'hello12', 'mypassword'], 'strong': ['python12345']}