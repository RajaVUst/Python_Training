def word_frequencies(path):
    frequencies = {}

    with open(path, "r") as f:
        for line in f:
            words = line.lower().split()

            for word in words:
                frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


frequencies = word_frequencies("../part_A/notes.txt")

print(frequencies)


#output:
'''{'python': 3, 'is': 3, 'easy': 2, 'to': 2, 'learn.': 1, 'it': 1, 'has': 1, 'a': 1, 'simple': 1, 'syntax.': 1, 'you': 1, 'can': 1, 'use': 1, 'it': 1, 'for': 1, 'web': 1, 'development.': 1}'''