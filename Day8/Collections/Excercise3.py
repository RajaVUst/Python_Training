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

print(long_words)

unique_words = {
    word.lower()
    for sentence in sentences
    for word in sentence.split()
}

print(unique_words)

# Output:
# ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']
# {'is', 'are', 'comprehensions', 'list', 'the', 'fun', 'blue', 'python', 'sky', 'handy'}