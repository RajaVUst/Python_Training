def unique_words(text):
    words = text.lower().split()
    unique = set(words)
    return sorted(unique)
text = "Python is easy and Python is powerful"
print(unique_words(text))

# output
# ['and', 'easy', 'is', 'powerful', 'python']