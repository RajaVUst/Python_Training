#Debug1 - IndentationError  
# print("Start")
#   print("Middle")
# print("End")

print("Start")
print("Middle")
print("End")


# Debug2 - Type Error
# age = 24
# message = "I am " + age + " years old"
# print(message)

age = 24
message = f"I am {age} years old"
print(message)


#Debug3 - Name Error
# username = "logesh"
# print(f"Welcome, {usernam}!")

username = "logesh"
print(f"Welcome, {username}!")


#Debug4 - Index Error
# word = "Python"
# print(word[6])

word = "Python"
print(word[5])


#Debug5 - Silent Logic Bug
# sentence = "one two three"
# word_list = sentence.split(",")
# print(f"Word count: {len(word_list)}")

sentence = "one two three"
word_list = sentence.split()
print(f"Word count: {len(word_list)}")