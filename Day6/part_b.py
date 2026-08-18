# Exercise 6: Write a fresh file
from constants import NOTES_FILE, DIARY_FILE

with open(DIARY_FILE, "w") as f:
    f.write("I learned how to read files in Python.\n")
    f.write("I learned how to write data to files.\n")
    f.write("I learned how to use loops effectively.\n")

with open(DIARY_FILE, "r") as f:
    print(f.read())
# Output:
# I learned how to read files in Python.
# I learned how to write data to files.
# I learned how to use loops effectively.


# Exercise 7: Append without overwriting
with open(DIARY_FILE, "a") as f:
    f.write("I learned how to append data to files.\n")

with open(DIARY_FILE, "r") as f:
    print(f.read())
# Output:
# I learned how to read files in Python.
# I learned how to write data to files.
# I learned how to use loops effectively.
# I learned how to append data to files.


# Exercise 8: Write numbers to a file
with open("squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i ** 2) + "\n")
total = 0
with open("squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())
print("Total:", total)
# Output:
# Total: 385


# Exercise 9: Copy and transform a file
with open(NOTES_FILE, "r") as source, open("notes_upper.txt", "w") as destination:
    for line in source:
        destination.write(line.upper())
with open("notes_upper.txt", "r") as f:
    print(f.read())
# Output:
# PYTHON IS EASY TO LEARN.
# FILES HELP STORE INFORMATION.
# READING FILES IS IMPORTANT.
# PRACTICE EVERY DAY.
# CODING IMPROVES SKILLS.