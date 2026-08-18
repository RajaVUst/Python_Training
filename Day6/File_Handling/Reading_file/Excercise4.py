# Line-by-line iteration

with open("Day6/notes.txt", "r") as f:

    for line in f:
        clean_line = line.strip()
        if not clean_line:
            continue
        print(clean_line.upper())

# Output:
# HELLO!
# I AM LEARNING PYTHON