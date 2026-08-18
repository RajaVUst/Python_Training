
def word_frequencies(path):
    freq = {}
    with open(path) as f:
        for line in f:
            for word in line.lower().split():
                freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequencies("notes.txt"))
#output
# {'python': 1, 'is': 3, 'a': 1, 'versatile': 1, 'programming': 1, 'language.': 1, 'it': 1, 'widely': 1, 'used': 1, 'for': 1, 'web': 1, 'development': 1, 'and': 2, 'data': 2, 'science.': 1, 'file': 1, 'handling': 1, 'lets': 1, 'programs': 2, 'read': 1, 'write': 1, 'on': 1, 'disk.': 1, 'exceptions': 1, 'help': 1, 'handle': 1, 'errors': 1, 'gracefully.': 1, 'practice': 1, 'the': 1, 'best': 1, 'way': 1, 'to': 1, 'master': 1, 'these': 1, 'concepts.': 1}