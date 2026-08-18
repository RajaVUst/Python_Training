with open("diary.txt", "a") as f:
    f.write("I learned about file handling.\n")

# Read and print the entire file
with open("diary.txt", "r") as f:
    content = f.read()

print(content)

"""
OUTPUT:
I learned how to read files in Python.
I learned how to write data to text files.
I learned how to use loops with file objects.
I learned about file handling.
"""