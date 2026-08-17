def unique_words(text):
    words = text.lower().split()
    unique = set(words)
    return sorted(unique)


sentence = "Python is easy and Python is powerful"

print(unique_words(sentence))

# output:
# ['and', 'easy', 'is', 'powerful', 'python']