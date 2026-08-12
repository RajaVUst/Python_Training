# Debug 1: IndentationError
print("Start")
print("Middle")
print("End")

# Debug 2: TypeError
age = 24
message = "I am " + str(age) + " years old"
print(message)

# Debug 3: NameError
username = "reni_k"
print(f"Welcome, {username}!")

# Debug 4: IndexError
word = "Python"
print(word[5])

# Debug 5: Silent Logic Bug
sentence = "one two three"
word_list = sentence.split()
print(word_list)
print(f"Word count: {len(word_list)}")