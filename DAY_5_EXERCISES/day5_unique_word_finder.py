def unique_words(text):
    words = text.lower().split()
    unique = set(words)
    return sorted(unique)


sentence = "The quick brown fox jumps over the lazy dog and the fox runs"
result = unique_words(sentence)

print(result)

"""
Output->
['and', 'brown', 'dog', 'fox', 'jumps', 'lazy', 'over', 'quick', 'runs', 'the']
"""