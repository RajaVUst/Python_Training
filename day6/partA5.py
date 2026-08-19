count = 0

with open("oneline.txt", "r") as f:
    for line in f:
        words = line.split()
        count = count + len(words)

print(f"Total words: {count}")

# OUTPUT

# Total words: 4