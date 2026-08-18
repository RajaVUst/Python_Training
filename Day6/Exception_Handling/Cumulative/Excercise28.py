# Word frequency counter

def word_frequencies(path):
    frequency = {}

    with open(path, "r") as f:
        for line in f:
            words = line.lower().split()
            
            for word in words:
                if word in frequency:
                    frequency[word] = frequency[word] + 1
                else:
                    frequency[word] = 1

    return frequency

result = word_frequencies("Day6/notes.txt")
print(result)


# Output:
# {'hello!': 1, 'i': 1, 'am': 1, 'learning': 1, 'python': 1}