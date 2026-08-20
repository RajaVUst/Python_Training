
sentences = [
    "the sky is blue",
    "python is fun",
    "list comprehensions are handy"
]

long_words = [
    word
    for sentence in sentences
    for word in sentence.split()
    if len(word) > 2
]

unique_words = {
    word.lower()
    for sentence in sentences
    for word in sentence.split()
}

print("Long words:", long_words)
print("Unique words:", unique_words)

# Output:
# Long words: ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']
# Unique words: {'the', 'sky', 'is', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy'}

#Checkpoint answer:
# A nested comprehension becomes less readable when there are many conditions,
# multiple levels of nesting, or complicated processing.
#
# Example:
# If a comprehension needs several nested loops and many if/else conditions,
# a normal for-loop is usually easier to understand and debug.