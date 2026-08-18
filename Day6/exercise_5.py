total_words = 0

with open("notes.txt", "r") as f:
    for line in f:
        words = line.split()
        total_words += len(words)
print(total_words)

# output
# 10