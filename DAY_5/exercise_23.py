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

passwords = ["abc", "hello1", "Secret!", "SuperSecure1", "pass", "Bootcamp9", "xyz"]

result = password_report(passwords)
print("Weak:  ", result["weak"])
print("Medium:", result["medium"])
print("Strong:", result["strong"])
