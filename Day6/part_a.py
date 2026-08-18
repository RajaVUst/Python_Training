from constants import NOTES_FILE

# Create notes.txt

with open(NOTES_FILE, "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("Files help store information.\n")
    f.write("Reading files is important.\n")
    f.write("Practice every day.\n")
    f.write("Coding improves skills.\n")


# Exercise 1: Read the whole file
with open(NOTES_FILE, "r") as f:
    content = f.read()
print("Length of file:", len(content))
# Output:
# Length of file: 127


# Exercise 2: Read just the first line
with open(NOTES_FILE, "r") as f:
    first_line = f.readline().strip()

print(first_line)
# Output:
# Python is easy to learn.


# Exercise 3: Read all lines into a list
with open(NOTES_FILE, "r") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))
print(lines)
# Output:
# Number of lines: 5
# ['Python is easy to learn.\n',
#  'Files help store information.\n',
#  'Reading files is important.\n',
#  'Practice every day.\n',
#  'Coding improves skills.\n']


# Exercise 4: Line-by-line iteration
with open(NOTES_FILE, "r") as f:
    for line in f:
        clean_line = line.strip()

        if not clean_line:
            continue

        print(clean_line.upper())
# Output:
# PYTHON IS EASY TO LEARN.
# FILES HELP STORE INFORMATION.
# READING FILES IS IMPORTANT.
# PRACTICE EVERY DAY.
# CODING IMPROVES SKILLS.


# Exercise 5: Count words in a file
word_count = 0
with open(NOTES_FILE, "r") as f:
    for line in f:
        word_count += len(line.split())
print("Total words:", word_count)
# Output:
# Total words: 19