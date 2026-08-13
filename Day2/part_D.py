# Exercise 7: Initials Generator
full_name = "Tuljesh Rahul"
first,last = full_name.split()
print(f"Initials are {first[0]}{last[0]}")

# Exercise 8: Loading Bar
full = "=" * 20
partial = "=" * 8 + "-" * 12
print(f"Full: {full} Partial: {partial}")

# Exercise 9: File Extension Checker
filename = "day2_notes.docx"
print(f"Whether ends with docx {filename.endswith(".docx")}")
print(f"Whether ends with pdf {filename.endswith(".pdf")}")

#Exercise 10: Find and Replace Report
text = "the quick brown fox"
index = text.find("brown")
print(f"Index of brown is {index}, Replaced: {text.replace("brown","red")}")

# Exercise 11: Username Validator
username = "reni_k99"
print(f"Is alphanumeric {username.isalnum()}")
print(f"Length is {len(username)}")
print(f"Whether valid length {len(username)>=6}")

# Exercise 12: Title Case vs Capitalize
phrase = "the quick brown fox"
print(phrase.title())
print(phrase.capitalize())

# Exercise 13: Receipt Line Formatter
item = "Notebook"
price = 149.0

print(f"{item:<15}|{price:>8.2f}")

# Exercise 14: Traceback Autopsy
# Exception type - ZeroDivisionError
# File - report.py
# line number - 4
# line of code failed - average = total / count
# root cause - count value is zero, so division by zero is not possible