#Debug 1  ·  IndentationError  
#print("Start")
 # print("Middle")
#print("End")

print("Start")
print("Middle")
print("End")



 # Debug 2  ·  TypeError  
#age = 24
#message = "I am " + age + " years old"
#print(message)

age = 24
print(f"I am {age} years old")

 # Debug 3  ·  NameError  
#username = "reni_k"
#print(f"Welcome, {usernam}!")

username = "reni_k"
print(f"Welcome, {username}!")

 # Debug 4  ·  IndexError  
#word = "Python"
#print(word[6])

word = "Python"
print(word[5])


 # Debug 5  ·  Silent Logic Bug (no traceback — use print())  
 # sentence = "one two three"
#word_list = sentence.split(",")
#print(f"Word count: {len(word_list)}")

sentence = "one two three"
word_list = sentence.split()

print("DEBUG:", word_list)
print(f"Word count: {len(word_list)}")


