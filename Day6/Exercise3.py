
with open("notes.txt") as f:
    lines = f.readlines()
print(len(lines))
print(lines)

#output
# 5
# ['Python is a versatile programming language.\n', 'It is widely used for web development and data science.\n', 'File handling lets programs read and write data on disk.\n', 'Exceptions help programs handle errors gracefully.\n', 'Practice is the best way to master these concepts.\n']