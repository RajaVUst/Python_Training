def unique_words(text):
    words = text.lower().split()
    return sorted(set(words))


sentence = "Python is fun and Python is powerful"
print(unique_words(sentence))

"""
OUTPUT:
['and', 'fun', 'is', 'powerful', 'python']
"""