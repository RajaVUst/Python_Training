sentences = ["the sky is blue", "python is fun", "list comprehensions are handy"]

long_words = [word for sentence in sentences for word in sentence.split() if len(word) > 2]
unique_words = {word.lower() for sentence in sentences for word in sentence.split()}

print(long_words)
print(unique_words)
# Output:
# ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']
# {'is', 'handy', 'list', 'are', 'python', 'comprehensions', 'sky', 'blue', 'the', 'fun'}
# Checkpoint: a nested comprehension gets hard to read once you need a 3rd
# level of nesting or more than one 'if' mixed with the nesting.