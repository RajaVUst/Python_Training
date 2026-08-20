sentences = ["the sky is blue", "python is fun", "list comprehensions are handy"]
list_of_strings=[word for sentence in sentences for word in sentence.split() if len(word)>2]
print(list_of_strings)
#output
#['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']