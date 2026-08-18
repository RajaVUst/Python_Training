# Exercise 6: Write a Fresh File

with open("diary.txt", "w") as f:
    f.write("I learned about lists and list operations.\n")
    f.write("I practiced tuples, sets, and dictionaries.\n")
    f.write("I completed file handling exercises in Python.\n")

print("Exercise 6 completed: diary.txt created.")
print()

# Exercise 7: Append Without Overwriting

with open("diary.txt", "a") as f:
    f.write("I learned how to read and write files.\n")

print("Contents of diary.txt:")

with open("diary.txt", "r") as f:
    print(f.read())

print()


# Exercise 8: Write Numbers to a File

with open("squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i ** 2}\n")

total = 0

with open("squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("Total of squares:", total)
print()


# Exercise 9: Copy and Transform a File

with open("notes.txt", "r") as source, open("notes_upper.txt", "w") as destination:
    for line in source:
        destination.write(line.upper())

print("notes_upper.txt created successfully.")


#output
'''Exercise 6 completed: diary.txt created.

Contents of diary.txt:
I learned about lists and list operations.
I practiced tuples, sets, and dictionaries.
I completed file handling exercises in Python.
I learned how to read and write files.


Total of squares: 385

notes_upper.txt created successfully.'''