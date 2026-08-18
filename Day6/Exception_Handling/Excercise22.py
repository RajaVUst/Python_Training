# Use finally for cleanup logging

try:
    with open("Day6/notes.txt", "r") as f:
        data = f.read()
    print(data)

except FileNotFoundError:
    print("File not found.")

finally:
    print("Attempt finished")

#Output:
# Hello!
# I am learning python

# Attempt finished