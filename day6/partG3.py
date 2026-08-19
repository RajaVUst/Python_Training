import string


def word_frequencies(path):
    frequencies = {}
    with open(path, "r") as f:
        content = f.read()
        words = content.lower().split()

        for word in words:
            word = word.strip(string.punctuation)
            if word:
                frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


print(word_frequencies("notes.txt"))

# OUTPUT

# {'python': 1, 'makes': 1, 'file': 1, 'handling': 1, 'simple': 1, 'practice': 1, 'builds': 1, 'confidence': 1}
