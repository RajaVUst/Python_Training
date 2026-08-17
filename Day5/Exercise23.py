
def password_report(passwords):
    report = {"weak": [], "medium": [], "strong": []}
    for pw in passwords:
        has_digit = any(ch.isdigit() for ch in pw)
        if len(pw) >= 10 and has_digit:
            report["strong"].append(pw)
        elif len(pw) >= 6:
            report["medium"].append(pw)
        else:
            report["weak"].append(pw)
    return report
 
sample_passwords = ["abc", "password", "Str0ngPass1", "hello6", "SuperSecure99"]
print(password_report(sample_passwords))
# {'weak': ['abc'], 'medium': ['password', 'hello6'],'strong': ['Str0ngPass1', 'SuperSecure99']}