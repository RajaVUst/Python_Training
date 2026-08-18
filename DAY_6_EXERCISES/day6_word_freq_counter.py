def word_frequencies(path):
    frequencies = {}

    with open(path, "r") as f:
        for line in f:
            words = line.lower().split()

            for word in words:
                frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


result = word_frequencies("DAY_6_EXERCISES/note.txt")
print(result)

"""
Output->
{
'hello': 1, 'from': 1, 'notes': 1, 'file.': 1, 'python': 1, 'file': 1, 'handling': 1, 'is': 2,
 'useful.': 1, 'this': 1, 'the': 1, 'third': 1, 'line.': 1, 'practice': 1, 'makes': 1, 
 'coding': 1, 'easier.': 1, 'end': 1, 'of': 1, 'sample': 1, 'notes.': 1
}
"""
