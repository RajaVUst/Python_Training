# Indentation Error 
print("Start") 
print("Middle") 
print("End") 

# Type Error
age = 24 
message = "I am " + str(age) + " years old" 
print(message) 

# Name Error
username = "reni_k" 
print(f"Welcome, {username}!") 

# Index Error
word = "Python" 
print(word[5]) 

# Silent Logic Bug
sentence = "one two three" 
word_list = sentence.split() 
print(f"Word count: {len(word_list)}") 

"""
Output ->
Start
Middle
End
I am 24 years old
Welcome, reni_k!
n
Word count: 3
"""