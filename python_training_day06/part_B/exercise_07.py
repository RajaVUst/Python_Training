with open("diary.txt", "a") as f:
    f.write("I practiced CSV and JSON files.\n")

with open("diary.txt", "r") as f:
    content = f.read()

print(content)


#output:
'''I learned Python file handling.
I learned about exceptions.
I practiced reading and writing files.
I practiced CSV and JSON files.'''