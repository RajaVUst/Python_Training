with open("DAY_6_EXERCISES/note.txt", "r") as f:
    total_words = 0

    for line in f:
        total_words += len(line.split())

print("Total words:", total_words)

"""
Output->
Total words: 22
"""
