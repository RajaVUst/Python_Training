sentences = ["the sky is blue", "python is fun", "list comprehensions are handy"]


long_words = [word for sentence in sentences for word in sentence.split() if len(word) > 2]

print(long_words)

#OUTPUT

# ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']
