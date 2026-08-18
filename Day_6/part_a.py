# Exercise 1
with open("notes.txt", "r") as f:
    content = f.read()

print("Character count:", len(content))
print()

# Exercise 2
with open("notes.txt", "r") as f:
    first_line = f.readline().strip()

print("First line:", first_line)
print()

# Exercise 3
with open("notes.txt", "r") as f:
    lines = f.readlines()

print("Number of lines:", len(lines))
print(lines)
print()

# Exercise 4
print("Non-blank lines in uppercase:")
with open("notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()

        if not clean_line:
            continue

        print(clean_line.upper())

print()

# Exercise 5
word_count = 0

with open("notes.txt", "r") as f:
    for line in f:
        word_count += len(line.split())

print("Total words:", word_count)


#Output
'''Character count: 282
First line: Python is a popular programming language.

Number of lines: 7
['Python is a popular programming language.\n', '\n', 'It is used for web development, data analysis, automation, and machine learning.\n', 'Files allow programs to store and retrieve information.\n', 'Reading files is an important Python skill.\n', '\n', 'Practice every day to improve your programming abilities.']

Non-blank lines in uppercase:
PYTHON IS A POPULAR PROGRAMMING LANGUAGE.
IT IS USED FOR WEB DEVELOPMENT, DATA ANALYSIS, AUTOMATION, AND MACHINE LEARNING.
FILES ALLOW PROGRAMS TO STORE AND RETRIEVE INFORMATION.
READING FILES IS AN IMPORTANT PYTHON SKILL.
PRACTICE EVERY DAY TO IMPROVE YOUR PROGRAMMING ABILITIES.

Total words: 41
'''