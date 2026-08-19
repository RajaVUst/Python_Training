with open("diary.txt", "a") as f:
    f.write("I learned how append mode preserves existing content.\n")

with open("diary.txt", "r") as f:
    content = f.read()

print(content)

# OUTPUT

# I learned how to read files in Python.
# I learned how to write text to files.
# I learned how to handle exceptions.
# I learned how append mode preserves existing content.
