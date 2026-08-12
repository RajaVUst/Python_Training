sentence = ' I am pavan from hyderabad '
clean = sentence.strip()
print(clean)
print(clean.lower())
print(clean.upper())
print(clean[0])
print(clean[-1])
print(clean[:5])
words = clean.split()
print(words)
print(len(words))
print(clean.replace("Fun", "Powerful"))
print("-".join(words))
print(f"words : {len(words)} || reverse : {clean[::-1]}")
#Debug 3  ·  NameError  
username = "reni_k"
print(f"Welcome, {username}!")

#Debug 4  ·  IndexError  
word = "Python"
print(word[5])

#debug 5
sentence2 = "one two three"
word_list = sentence2.split()
print(f"Word count: {len(word_list)}")

#excercise 1
first_name = input("Enter your first_name : ")
last_name = input("Enter your last_name : ")
full = first_name +" " + last_name
full=full.title()
print(f"Hello! {full}") 

#excersice 2
code = "PYTHON2026SALE"
print(code[ :6])
print(code[-4: ])
print(code[::-1])

#excersie 3
word2 = 'pavap'
palindrome = word2[::-1]
if palindrome == word2:
    print("IS palindrome")
else: 
    print("Not a palindrome")  
#excersie 4
email = input("Enter email:")
username , domain = email.split('@')
print('username :',username)
print('domain : ',domain)
#excersie 5
Given_title = "  My First   Python Project!!  "
step1 = Given_title.strip()
step2 = step1.replace('!!','')
step3 = step2.lower()
step4 = step3.replace(' ','_')
print(step4)


#excersie 6
sentence = input("Enter any sentence : ")
characters = len(sentence)
words = len(sentence.split())
vowel = sentence.count('a') +sentence.count('e')+sentence.count('i')+sentence.count('o')+sentence.count('u')
character_length = characters>30
print("No of characters :",characters)
print("No of vowel :",vowel)
print("No of words :",words)
print("length is greater 30 :",character_length)


#excersie 7
full_name = input("Enter full name: ")
first_name ,last_name = full_name.split(" ")
print(f"{first_name[0]}{last_name[0]}")


#excersie 8
Full = "=" * 20
partial = "=" * 8 + "-" * 12
print(f"full : {Full}")
print(f"partial :{partial}")


#excersie 9
filename = "day2_notes.docx"
pdf = filename.endswith(".pdf")
doc = filename.endswith(".docx")
print(pdf)
print(doc)


#excersice 10

text = "the quick brown fox"
findd = text.find('brown')
print(findd)
new_text = text.replace('brown','red')
print(new_text)

#excersice 11

username = "reni_k99"
alpha = username.isalnum()
length = len(username)
minlength = length>6
print(f"Is the username is alphanumeric or not : {alpha}")
print(f"length of the username : {length}")
print(f"Is the username length is greater than 6 or not : {minlength}" )

#excersie 12
phrase = "the quick brown fox"
print(phrase.title())
print(phrase.capitalize())

#excersie 13
price = 149.3444
item = "Notebook"
print(f" {item:<15} || {price:>15.2f}")





