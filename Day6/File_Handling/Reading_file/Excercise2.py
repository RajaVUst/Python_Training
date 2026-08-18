# Read just first line

with open("Day6/notes.txt", "r") as f:
    line = f.readline()
print(line.strip())

# Output:
# Hello!