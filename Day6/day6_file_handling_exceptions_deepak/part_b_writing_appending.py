# Exercise 6 - Write a fresh file
with open("diary.txt", "w") as f:
    f.write("I learned how to open and read files.\n")
    f.write("I learned the difference between write and append mode.\n")
    f.write("I learned to use the with statement for safety.\n")
print("diary.txt created")
# Output: diary.txt created

# Exercise 7 - Append without overwriting
with open("diary.txt", "a") as f:
    f.write("I learned to work with csv and json files.\n")

with open("diary.txt", "r") as f:
    print(f.read())
# Output:
# I learned how to open and read files.
# I learned the difference between write and append mode.
# I learned to use the with statement for safety.
# I learned to work with csv and json files.

# Exercise 8 - Write numbers to a file
with open("squares.txt", "w") as f:
    for n in range(1, 11):
        f.write(str(n * n) + "\n")

total = 0
with open("squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())
print(total)
# Output: 385

# Exercise 9 - Copy and transform a file
with open("notes.txt", "r") as source, open("notes_upper.txt", "w") as dest:
    for line in source:
        dest.write(line.upper())

with open("notes_upper.txt", "r") as f:
    print(f.read())
# Output:
# PYTHON IS A BEGINNER-FRIENDLY LANGUAGE.
# TODAY WE ARE LEARNING FILE HANDLING.
# FILES CAN BE READ, WRITTEN, AND APPENDED.