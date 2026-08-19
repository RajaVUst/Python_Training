def word_frequencies(path):
    frequencies = {}

    with open(path, "r") as f:
        for line in f:
            words = line.lower().split()

            for word in words:
                frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


print(word_frequencies("notes.txt"))

# output:
# {'hey': 1, 'there': 1, 'i': 1, 'am': 1, 
#  'chandrashekhar': 1, 'and': 1, 'this': 1, 'is': 1, 
#  'the': 1, '6th': 1, 'day': 1, 'of': 1, 'training': 1}