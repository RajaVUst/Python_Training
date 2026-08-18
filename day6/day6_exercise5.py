word_count = 0

with open("day6/notes.txt", "r") as f:
    for line in f:
        word_count += len(line.split())

print(word_count)

"""
OUTPUT:
4
"""