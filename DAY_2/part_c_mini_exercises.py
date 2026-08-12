# Part C - Mini-Exercises

# --- Exercise 1: Name Tag Formatter ---
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = (first_name + " " + last_name).title()
print(f"Hello, {full_name}!")

print("---")

# --- Exercise 2: Coupon Code Slicer ---
code = "PYTHON2026SALE"
print(f"First 6 chars : {code[:6]}")
print(f"Last 4 chars  : {code[-4:]}")
print(f"Reversed      : {code[::-1]}")

print("---")

# --- Exercise 3: Palindrome Checker ---
word = "level"
is_palindrome = (word == word[::-1])
print(f"'{word}' is a palindrome: {is_palindrome}")

print("---")

# --- Exercise 4: Email Splitter ---
email = "reni.k@company.com"
username, domain = email.split("@")
print(f"Username : {username}")
print(f"Domain   : {domain}")

print("---")

# --- Exercise 5: Slug Normalizer ---
title = "  My First   Python Project!!  "
slug = title.strip().replace("!!", "").lower().replace(" ", "_")
print(f"Slug: {slug}")

print("---")

# --- Exercise 6: Sentence Dashboard ---
sentence = "Python is a powerful programming language"
char_count = len(sentence)
word_count = len(sentence.split())
vowel_count = (sentence.count('a') + sentence.count('e') +
               sentence.count('i') + sentence.count('o') +
               sentence.count('u'))
is_long = char_count > 30

print(f"Character count : {char_count}")
print(f"Word count      : {word_count}")
print(f"Vowel count     : {vowel_count}")
print(f"Longer than 30  : {is_long}")
