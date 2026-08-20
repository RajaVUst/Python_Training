sentences = ["the sky is blue", "python is fun", "list comprehensions are handy"]

long_words=[word for word in sentences for word in word.split() if len(word) >3]
unique_words={word for word in sentences for word in word.split()}

print("List of long words (length > 3):", long_words)
print("Set of unique words:", unique_words)

# Output:
# List of long words (length > 3): ['blue', 'python', 'list', 'comprehensions', 'handy']
# Set of unique words: {'the', 'list', 'sky', 'are', 'handy', 'comprehensions', 'python', 'is', 'blue', 'fun'}