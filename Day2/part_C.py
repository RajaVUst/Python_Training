# Exercise 1: Name Tag Formatter
first = input("Enter first name: ")
last = input("Enter last name: ")

print(f"Hello, {first.title()} {last.title()}!")

# Exercise 2: Coupon Code Slicer
code = "PYTHON2026SALE"
print(code[:6])
print(code[-4:])
print(code[::-1])

# Exercise 3: Palindrome Checker
word = 'level'
print(f"Is {word} Palindrome {word == word[::-1]}")

# Exercise 4: Email Splitter
email = "reni.k@company.com"
items = email.split('@')
print(f"Username: {items[0]}, Domain: {items[1]}")

# Exercise 5: Slug Normalizer
title = " My First  Python Project!!  "
print(title.strip().replace("!!","").lower().replace(" ","_"))

# Exercise 6: Sentence Dashboard
sentence = title.strip()
print(f"Character count {len(sentence)}")
print(f"Word count {len(sentence.split())}")
print(f"Vowel count {sentence.count('a')+sentence.count('e')+sentence.count('i')+sentence.count('o')+sentence.count("u")}")
print(f"Longer than 30 {len(sentence)>30}")