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

print("Words longer than 2 characters:", long_words)
print("Unique words:", unique_words)

#output
'''

Words longer than 2 characters: ['the', 'sky', 'blue', 'python', 'fun', 'list', 'comprehensions', 'are', 'handy']
Unique words: {'the', 'sky', 'comprehensions', 'are', 'fun', 'handy', 'python', 'is', 'blue', 'list'}
'''
