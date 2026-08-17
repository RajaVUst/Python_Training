# Unique Word Finder

def unique_words(text):
    words = text.lower().split()
    unique = set(words)
    return sorted(unique)

text = "Python is easy and Python is useful"
print(unique_words(text))


# Output:
# ['and', 'easy', 'is', 'python', 'useful']