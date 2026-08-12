# Part B 

# Debug 1 - Indentation Error
print("Start")
print("Middle")
print("End")
print("\n" + "-" * 40)


# Debug 2 - TypeError
age = 24
message = "I am " + str(age) + " years old"

print(message)
print("\n" + "-" * 40)


# Debug 3 - NameError
username = "varsha_T"

print(f"Welcome, {username}!")
print("\n" + "-" * 40)


# Debug 4 - IndexError
word = "Python"

print(word[5])
print("\n" + "-" * 40)


# Debug 5 - Silent Logic Bug
sentence = "one two three"
word_list = sentence.split()

print("DEBUG:", word_list)
print(f"Word count: {len(word_list)}")