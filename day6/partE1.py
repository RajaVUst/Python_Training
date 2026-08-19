try:
    with open("ghost.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("file could not be found.")

# OUTPUT

# file could not be found.
