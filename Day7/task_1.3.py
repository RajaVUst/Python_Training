sentences = [ "the sky is blue", "python is fun", "list comprehensions are handy"]

# Flat list of words longer than 2 characters
long_words = [
    word
    for sentence in sentences
    for word in sentence.split()
    if len(word) > 2
]


print(long_words)

# ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']



# Unique words, case-insensitive
unique_words = {
    word.lower()
    for sentence in sentences
    for word in sentence.split()
}


print(unique_words)

# {'sky', 'the', 'handy', 'fun', 'python', 'blue', 'is', 'are', 'comprehensions', 'list'}