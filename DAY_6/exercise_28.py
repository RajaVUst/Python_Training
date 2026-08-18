def word_frequencies(path):
    frequencies = {}
    with open(path, "r") as f:
        for line in f:
            for word in line.lower().split():
                frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

result = word_frequencies("notes.txt")
print(result)
