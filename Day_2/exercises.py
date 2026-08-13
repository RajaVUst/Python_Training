#PART A
sentence = " Python is FUN To LeArn !! "

#whitespace
clean = sentence.strip()
print(clean)

#lowercase and uppercase
print(clean.lower())
print(clean.upper())

#indexing
print(clean[0])
print(clean[-1])
print(clean[0:5])

#split
split = clean.split()
print(len(split))

#replace
print(clean.replace("FUN" , "Intresting")) 

#join
print("-".join(split))

#f-string
print(f"Words: {len(split)} | Reversed: {clean[::-1]}")

#PART C

#  Exercise 1  ·  Name Tag Formatter  
first_name = input("Enter you first name : ")
last_name = input("Enter you last name : ")

print(f"Hey, {first_name.title()} {last_name.title()}!!!")

#Exercise 2  ·  Coupon Code Slicer  

code = "PYTHON2026SALE"
print(code[:6])
print(code[-4:])
print(code[::-1])

#Exercise 3  ·  Palindrome Checker  

word = "level"
is_palindrome = (word == word[::-1])
print(is_palindrome)

#Exercise 4  ·  Email Splitter  

email = "308262@ust.com"
username, domain = email.split("@")
print(f"Username: {username}")
print(f"Domain: {domain}")

#Exercise 5  ·  Slug Normalizer  

title = "  My First   Python Project!!  "

slug = title.strip()
print(slug)

slug = slug.replace("!!", "")
print(slug)

slug = slug.lower()
print(slug)

slug = slug.replace(" ", "_")
print(slug)

#  Exercise 6  ·  Sentence Dashboard  
sentence = input("Enter a sentence: ")

char_count = len(sentence)
word_count = len(sentence.split())

vowel_count = (
    sentence.count('a') +
    sentence.count('e') +
    sentence.count('i') +
    sentence.count('o') +
    sentence.count('u')
)

is_long = len(sentence) > 30

print(f"Character count: {char_count}")
print(f"Word count: {word_count}")
print(f"Vowel count: {vowel_count}")
print(f"Longer than 30 characters: {is_long}")

#PART D

#Exercise 7  ·  Initials Generator 

full_name = "Mary Jane"

words = full_name.split()
initials = words[0][0] + words[1][0]

print(initials)

#Exercise 8 · Loading Bar

print(f"Full: {'=' * 20}")
print(f"Partial: {'=' * 8 + '-' * 12}")

#Exercise 9 · File Extension Checker

filename = "day2_notes.docx"

print(filename.endswith(".docx"))
print(filename.endswith(".pdf"))

#Exercise 10 · Find and Replace Report

text = "the quick brown fox"

index = text.find("brown")
new_text = text.replace("brown", "red")

print(f"Original text: {text}")
print(f"Index found: {index}")
print(f"New text: {new_text}")

#Exercise 11 · Username Validator (Facts Only)

username = "jay_9099"

print(username.isalnum())
print(len(username))
print(len(username) >= 6)

#Exercise 12 · Title Case vs. Capitalize

phrase = "the quick brown fox"
print(f"Title: {phrase.title()}")
print(f"Capitalize: {phrase.capitalize()}")

#Exercise 13 · Receipt Line Formatter

item = "Notebook"
price = 149.0
print(f"{item:<15}|{price:>8.2f}")

#Exercise 14 · Traceback Autopsy

#Traceback (most recent call last):
#  File "report.py", line 4, in <module>
#       average = total / count
#ZeroDivisionError: division by zero
        


#ZeroDivisionError
#File "report.py", line 4
#average = total / count
#The variable count had a value of 0, and Python cannot divide a number by zero.
