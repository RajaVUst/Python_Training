def password_report(passwords):
    report = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for password in passwords:
        contains_digit = any(
            character.isdigit()
            for character in password
        )

        if len(password) >= 10 and contains_digit:
            report["strong"].append(password)
        elif len(password) >= 6:
            report["medium"].append(password)
        else:
            report["weak"].append(password)

    return report


sample_passwords = [
    "abc",
    "hello1",
    "python",
    "SecurePass9",
    "LongPassword",
    "Code123456"
]

print(password_report(sample_passwords))

'''
output:
{
'weak': ['abc'], 
'medium': ['hello1', 'python', 'LongPassword'], 
'strong': ['SecurePass9', 'Code123456']
}


'''