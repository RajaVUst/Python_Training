try:
    with open("notes.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File loaded successfully.")
    print("Length:", len(content))
