def word_frequencies(path):
    frequencies = {}

    with open(path, "r") as f:
        text = f.read().lower()

    for word in text.split():
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies

print(word_frequencies("day6/notes.txt"))

"""
OUTPUT:
{'hello': 1, 'world!!!': 1, 'good': 1, 'morning': 1}
"""