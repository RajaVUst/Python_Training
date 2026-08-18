# Day 6 - Exercise 28

import string


def word_frequencies(path):
    frequencies = {}

    try:
        with open(path, "r") as f:
            for line in f:
                words = line.lower().split()

                for word in words:
                    word = word.strip(string.punctuation)

                    if word:
                        frequencies[word] = frequencies.get(word, 0) + 1

    except FileNotFoundError:
        print(f"{path} was not found.")
        return {}

    return frequencies


print(word_frequencies("notes.txt"))

#output
'''
{'aws': 1, 'is': 1, 'the': 2, 'most': 1, 'used': 1, 'cloud': 1, 'platform': 1, 'it': 1, 'has': 1, 'many': 1, 'data': 1, 'centers': 1, 'around': 1, 'world': 1, 'today': 1, 'i': 2, 'learnt': 2, 'about': 2, 'ec2': 2, 'and': 2, 's3': 2, 'bucketstoday': 1, 'buckets': 1}

'''

