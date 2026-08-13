#Part A
text=" Python IS Fun to Learn!!  "
clean=text.strip();
print(clean);
print(clean.lower());
print(clean.upper());
print(clean[0]);
print (clean[-1]);
print(clean[0:5]);
list_of_words=clean.split();
print(list_of_words);
print(len(list_of_words));
print(clean.replace("Fun","Powerful"));
print("-".join(list_of_words));
print(f"Words:{len(list_of_words)} | Reversed:{clean[::-1]}");


#Part C
#Q1
first_name=input("Enter your first name: ");
last_name=input("Enter your last name: ");
print(f"First Name: {first_name.title()}, Last Name: {last_name.title()}");

#Q2
code="PYTHON2026SALE"
print(code[0:6]);
print(code[-4:]);
print(code[::-1]);

# Q3
word = "level"
is_palindrome = (word == word[::-1])
print(is_palindrome)

# Q4
email = "reni.k@company.com"
username, domain = email.split("@")
print(f"Username: {username}")
print(f"Domain: {domain}")

# Q5
title = "  My First   Python Project!!  "
slug = title.strip()
slug = slug.replace("!!", "")
slug = slug.lower()
slug = slug.replace(" ", "_")
print(slug)

# Q6
sentence = "Python is fun to learn and practice"

print(f"Character Count: {len(sentence)}")
print(f"Word Count: {len(sentence.split())}")

vowel_count = (
    sentence.count("a")
    + sentence.count("e")
    + sentence.count("i")
    + sentence.count("o")
    + sentence.count("u")
)

print(f"Vowel Count: {vowel_count}")
print(f"Longer than 30 characters: {len(sentence) > 30}")


#Part D
# Q7
full_name = "Reni Kumar"
words = full_name.split()
initials = words[0][0] + words[1][0]
print(f"Initials: {initials}")

# Q8
print(f"Full: {'=' * 20}")
print(f"Partial: {'=' * 8 + '-' * 12}")

# Q9
filename = "day2_notes.docx"
print(filename.endswith(".docx"))
print(filename.endswith(".pdf"))

# Q10
text = "the quick brown fox"
index = text.find("brown")
new_text = text.replace("brown", "red")

print(f"Original Text: {text}")
print(f"Index Found: {index}")
print(f"New Text: {new_text}")

# Q11
username = "reni_k99"
print(username.isalnum())
print(len(username))
print(len(username) >= 6)

# Q12
phrase = "the quick brown fox"
print(f"Title: {phrase.title()}")
print(f"Capitalize: {phrase.capitalize()}")

# Q13
item = "Notebook"
price = 149.0
print(f"{item:<15}|{price:>8.2f}")

# Q14
print("Exception Type: ZeroDivisionError")
print("File and Line: report.py, line 4")
print("Failed Line: average = total / count")
print("Cause: Division by zero occurred because count was 0.")