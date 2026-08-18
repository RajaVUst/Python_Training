# Day 6 - Exercise 21

try:
    with open("notes.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("The file was not found.")

else:
    print("File loaded successfully.")
    print("File length:", len(content))

#output
'''
File loaded successfully.
File length: 156
'''


