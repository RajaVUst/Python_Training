#Exercise 1 — Name Tag Formatter
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {first_name.title()} {last_name.title()}!")
 
#Exercise 2 — Coupon Code Slicer
code = "PYTHON2026SALE"
print(code[:6])
print(code[-4:])
print(code[::-1])
 
#Exercise 3 — Palindrome Checker
word = "level"
is_palindrome = (word == word[::-1])
print(is_palindrome)
 
#Exercise 4 — Email Splitter
email = "navyasamudrala@company.com"
username, domain = email.split("@")
print(f"Username: {username}")
print(f"Domain: {domain}")
 
#Exercise 5 — Slug Normalizer
title = "  My First   Python Project!!  "
slug = title.strip().replace("!!", "").lower().replace(" ", "_")
print(slug)
 
#Exercise 6 — Sentence Dashboard
sentence = "Python is fun to learn and easy to use"
char_count = len(sentence)
word_count = len(sentence.split())
vowel_count = sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
is_long = len(sentence) > 30
 
print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"Vowels: {vowel_count}")
print(f"Longer than 30 chars: {is_long}")
 
# Exercise 7 - Initials Generator
full_name = "Reni Kumar"
first, last = full_name.split()
print(first[0] + last[0])
 
# Exercise 8 - Loading Bar
print("Full:", "=" * 20)
print("Partial:", "=" * 8 + "-" * 12)
 
# Exercise 9 - File Extension Checker
filename = "day2_notes.docx"
print(filename.endswith(".docx"))
print(filename.endswith(".pdf"))
 
# Exercise 10 - Find and Replace Report
text = "the quick brown fox"
index = text.find("brown")
new_text = text.replace("brown", "red")
 
print(f"Original: {text}")
print(f"Index found: {index}")
print(f"New text: {new_text}")
 
# Exercise 11 - Username Validator (Facts Only)
username = "DeepakNethaji123"
print(username.isalnum())
print(len(username))
print(len(username) >= 6)
 
# Exercise 12 - Title Case vs. Capitalize
phrase = "the quick brown fox"
print(phrase.title())
print(phrase.capitalize())
 
# Exercise 13 - Receipt Line Formatter
item = "Notebook"
price = 149.0
print(f"{item:<10}|{price:>8.2f}")
 
# Exercise 14 - Traceback Autopsy
# Exception type: ZeroDivisionError
# File and line: report.py, line 4
# Failed line: average = total / count
# Root cause: count is 0 when the division runs, and Python doesn't allow dividing by zero.