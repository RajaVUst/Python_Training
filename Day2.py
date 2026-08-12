#Exercise 1 Name Tag Formatter
firstname=input("Enter Your firstname")
lastname=input("Enter Your lastname")
print(f"Name: {firstname.title()} {lastname.title()}")

#Exercise 2 Coupon Code Slicer
code = "PYTHON2026SALE"
print(code[:6])
print(code[-4:])
print(code[::-1])

#Excercise 3 Palindrome Checker
word='level'
is_palindrome = (word == word[::-1])
print(is_palindrome)

#Excercise 4 Email Spliter
email = "YeshwanthManekari@ust.com"
username, domain = email.split("@")
print(f"Username: {username}")
print(f"Domain: {domain}")

#Excercise 5 slug normalizer
title = " My First Python Project!! "
print(title.strip())
print(title.replace("!!", ""))
print(title.lower())
print(title.replace(" ", "_"))

#Excercise 6 sentence Dashboard
sentence = "Python is a great programming language."
word_count = len(sentence.split())
longerthan=word_count>30
vowel_count=sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
print(f"Word Count: {word_count}")
print(f"Vowel Count: {vowel_count}")
print(f"Is the sentence longer than 30 characters? {longerthan}")

#Excercise 7 Initials Generator
full_name=input("Enter your full name: ")
firstname,lastname=full_name.split()
initials = firstname[0].upper() + lastname[0].upper()
print(f"Initials: {initials}")

#Excercise 8 Loading Bar
full_bar="="*20
partial_bar="="*8 + "-"*12
print(f"Full Bar: {full_bar}")
print(f"Partial Bar: {partial_bar}")

#Excercise 9 File Extension Checker
filename = input("Enter a filename: ")
is_docx=filename.endswith(".docx")==True
is_pdf=filename.endswith(".pdf")==True
print(f"Is the file a .docx file? {is_docx}")
print(f"Is the file a .pdf file? {is_pdf}")

#Excercise 10 Find and Replace Report
text="the quick brown fox"
index_word=text.find("brown")
new_text=text.replace("brown","red")
print(f"Index of 'brown': {index_word}")
print(f"New text: {new_text}")
print(f"Original text: {text}")

#Excercise 11 Username Validator
username = "reni_k99"
is_alnum = username.isalnum()
length = len(username) > 0
lengthgreaterthan5 = len(username) > 6
print(f"Is the username alphanumeric? {is_alnum}")
print(f"Is the username length greater than 0? {length}")
print(f"Is the username length greater than 6? {lengthgreaterthan5}")

#Excercise 12 Title Case vs Capitalize
sentence = "python is a great programming language."
title_case = sentence.title()
capitalize_case = sentence.capitalize()
print(f"Title Case: {title_case}")
print(f"Capitalize Case: {capitalize_case}")

#Excercise 13 Recceipt line Formatter
item ="notebook"
price=149.00000
print(f"{item:<15}|{price:>8.2f}")