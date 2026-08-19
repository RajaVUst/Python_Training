try:
    with open("read.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("The file could not be found.")
else:
    print("File loaded successfully")
    print("File length:", len(content))

# OUTPUT

# File loaded successfully
# File length: 41
