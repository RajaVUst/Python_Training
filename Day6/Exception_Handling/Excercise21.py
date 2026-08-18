 # Use else

try:

    with open("Day6/notes.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")

else:

    print("File loaded successfully")
    print("File length:", len(data))

# Output:
# File loaded successfully
# File length: 28