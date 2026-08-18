# Exercise 6 - Write a fresh file
with open("diary.txt", "w") as f:
    f.write("Learned about file handling today\n")
    f.write("Practiced reading and writing text files\n")
    f.write("Understood the difference between read and write modes\n")


# Exercise 7 - Append without overwriting
with open("diary.txt", "a") as f:
    f.write("Feeling confident about today's topic\n")

with open("diary.txt", "r") as f:
    print(f.read())
# Output:
# Learned about file handling today
# Practiced reading and writing text files
# Understood the difference between read and write modes
# Feeling confident about today's topic


# Exercise 8 - Write numbers to a file
with open("squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i ** 2}\n")

total = 0
with open("squares.txt", "r") as f:
    for line in f:
        total += int(line)

print(total)
# Output: 385


# Exercise 9 - Copy and transform a file
with open("notes.txt", "r") as source, open("notes_upper.txt", "w") as destination:
    for line in source:
        destination.write(line.upper())