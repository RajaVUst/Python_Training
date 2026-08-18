def word_frequencies(path):
    frequencies = {}
    with open(path, "r") as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies
result = word_frequencies("notes.txt")
print(result)

# output
# {'hello': 1, 'world': 1, 'i': 1, 'am': 1, 'learning': 1, 'python': 1, 'today': 1, 'is': 1, 'day': 1, '6': 1}