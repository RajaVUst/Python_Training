# Setup: create notes.txt with 5 sample lines
with open("notes.txt", "w") as f:
    f.write("Python is a beginner-friendly language.\n")
    f.write("Today we are learning file handling.\n")
    f.write("Files can be read, written, and appended.\n")
    f.write("Exceptions help programs avoid crashing.\n")
    f.write("Practice is the key to mastering this topic.\n")

# Exercise 1 - Read the whole file
with open("notes.txt", "r") as f:
    whole_text = f.read()
print(len(whole_text))
# Output: 205

# Exercise 2 - Read just the first line
with open("notes.txt", "r") as f:
    first_line = f.readline().strip()
print(first_line)
# Output: Python is a beginner-friendly language.

# Exercise 3 - Read all lines into a list
with open("notes.txt", "r") as f:
    all_lines = f.readlines()
print(len(all_lines))
print(all_lines)
# Output:
# 5
# ['Python is a beginner-friendly language.\n', 'Today we are learning file handling.\n',
#  'Files can be read, written, and appended.\n', 'Exceptions help programs avoid crashing.\n',
#  'Practice is the key to mastering this topic.\n']

# Exercise 4 - Line-by-line iteration
with open("notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        if not clean_line:
            continue
        print(clean_line.upper())
# Output:
# PYTHON IS A BEGINNER-FRIENDLY LANGUAGE.
# TODAY WE ARE LEARNING FILE HANDLING.
# FILES CAN BE READ, WRITTEN, AND APPENDED.
# EXCEPTIONS HELP PROGRAMS AVOID CRASHING.
# PRACTICE IS THE KEY TO MASTERING THIS TOPIC.

# Exercise 5 - Count words in a file
total_words = 0
with open("notes.txt", "r") as f:
    for line in f:
        total_words += len(line.split())
print(total_words)
# Output: 31