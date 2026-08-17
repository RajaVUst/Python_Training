def unique_words(text):
    words = text.lower().split()
    unique = set(words)
    return sorted(unique)


# Test sentence with repeated words
text = "Python is easy and Python is powerful"

result = unique_words(text)

print(result)
#output
"""
['and', 'easy', 'is', 'powerful', 'python']"""