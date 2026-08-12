#PART-1
# sentence="   Python IS Fun to Learn!!   "
# clean=sentence.strip()
# print(clean.lower())
# print(clean.upper())
# print(clean[0])
# print(clean[-1])
# print(clean[:5])
# words=sentence.split()
# print(words)
# print(len(words))
# replce_word=sentence.replace("Fun", "Powerful")
# print(replce_word)

# join_words=['python','is','very','important']
# jn="-".join(join_words)
# print(jn)  
# print(f"Total words:{len(clean):<10}Reversed sting:{clean[::-1]:>10}")



#PART-B
#1
# print("Start")
# print("Middle")
# print("End")



# age = 24
# message = "I am " + str(age) + " years old"
# print(message)
# print(f"I am {age} years old")



# username = "reni_k"
# print(f"Welcome, {username}!")


# word = "Python"
# print(word[5])


# sentence = "one two three"
# word_list = sentence.split()
# print(word_list)
# print(f"Word count: {len(word_list)}")



#PART-C
#exe-----1

# first_name=input("Enter first name:")
# last_name=input("Enter last name:")
# full_name=first_name+" "+last_name
# full_name=full_name.title()
# print(f"Hello {full_name} !!!")


#exe----2
# coupon= "PYTHON2026SALE" 
# print(coupon[:6])
# print(coupon[-4:])
# print(coupon[::-1])

#exe----3
# word=input("Enter the value:")
# is_palindrome=(word==word[::-1])
# print(is_palindrome)

#exe--------4
# mail="boyini@surendra.com"
# username,domain=mail.split("@")
# print(f"Username:{username}")
# print(f"Domain:{domain}")



#exe--------5
# url="  My First   Python Project!!  "
# url=url.strip().lower().replace("!!","").replace(" ","_")
# print(url)


#exe--------6
# sentence=input("Enter the sentence:")
# characters=len(sentence)
# words=len(sentence.split())
# vowels=sentence.count("a")+sentence.count("e")+sentence.count("i")+sentence.count("o")+sentence.count("u")
# longer_than_30=len(sentence)>30
# print(f"Total characters:{characters}")
# print(f"Total words:{words}")
# print(f"Total vowels:{vowels}")
# print(f"LOnger than 30:{longer_than_30}")


#PART D
#exe-----7
# full_name=input("Enter the full name:")
# full_name=full_name.split()
# intials=full_name[0][0]+full_name[1][0]
# print(intials)


#exee-8
# full="=" * 20
# partial="=" * 8 + "-" * 12 
# print(f"Fill: {full}")
# print(f"Partial: {partial}")


#exe-----9
# file_name="day2_notes.pdf"
# is_dox=file_name.endswith(".docx")
# is_pdf=file_name.endswith(".pdf")
# print(is_dox)
# print(is_pdf)


#exeee----10
# text="the quick brown fox"
# index=text.find("brown")
# new_text=text.replace("brown","red")
# print(f"Original text:{text}")
# print(f"Index:{index}")
# print(f"New text:{new_text}")



#exe-----11
# username="djfgudygfuy4658734659"
# is_alpha_numeric=username.isalnum()
# length=len(username)
# at_least_6=(length>=6)
# print(f"Is it alphanumneric:{is_alpha_numeric}")
# print(f"Lenght of username:{length}")
# print(f"Is username have at least 6 charcters:{at_least_6}")


#exe----12
# senetence="the quick brown fox"
# sentence_title=senetence.title()
# senetence_capitalize=senetence.capitalize()
# print(f"Title checking: {sentence_title}")
# print(f"Capitals checking: {senetence_capitalize}")


#exee----13
item="Note Book"
price=149.0087458
print(f"{"items":<15}{"Prices":>10}")
print(f"{item:<15}|{price:>10.2f}")