
with open("notes.txt") as f:
    total_words = 0
    for line in f:
        total_words += len(line.split())
print(total_words)

#output
# 41