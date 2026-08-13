#indentation error 
print("Start")
print("Middle") 
print("End")

#type error
age = 24
message = "I am" + str(age) + "years old"
print(message)

#Name error
username = "reni_k"
print(f'welcome, {username}')

#index error
word = "Python"
print(word[5])

#Silent logice bug
sentence = 'one two three'
word_list = sentence.split(" ")
# print(f'DEBUG word_list: {word_list}')
print(f'Word count:{len(word_list)}')