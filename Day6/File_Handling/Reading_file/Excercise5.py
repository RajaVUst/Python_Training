# Count words in a file

count = 0
with open("Day6/notes.txt", "r") as f:

    for line in f:
        words = line.split()
        count = count + len(words)
print("Total words:", count)


#Output:
# Total words: 5