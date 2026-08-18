def word_frequencies(path):
    frequencies = {}

    with open(path, "r") as f:
        content = f.read()

    words = content.lower().split()

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


result = word_frequencies("notes.txt")

print(result)

# {'hello': 1, 'world': 1}
