# Exercise 1 - Read the whole file
with open("notes.txt", "r") as f:
    content = f.read()

print(len(content))
# Output: 187


# Exercise 2 - Read just the first line
with open("notes.txt", "r") as f:
    first_line = f.readline().strip()

print(first_line)
# Output: Started learning Python this week


# Exercise 3 - Read all lines into a list
with open("notes.txt", "r") as f:
    lines = f.readlines()

print(len(lines))
print(lines)
# Output:
# 5
# ['Started learning Python this week\n', 'Practiced loops and conditionals\n', 'Built small scripts daily\n', 'Learning file handling now\n', 'Excited for the next module\n']


# Exercise 4 - Line-by-line iteration
with open("notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        if not clean_line:
            continue
        print(clean_line.upper())
# Output:
# STARTED LEARNING PYTHON THIS WEEK
# PRACTICED LOOPS AND CONDITIONALS
# BUILT SMALL SCRIPTS DAILY
# LEARNING FILE HANDLING NOW
# EXCITED FOR THE NEXT MODULE


# Exercise 5 - Count words in a file
with open("notes.txt", "r") as f:
    total_words = 0
    for line in f:
        total_words += len(line.split())

print(total_words)
# Output: 26