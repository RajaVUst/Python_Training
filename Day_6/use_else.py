try:
    with open("notes.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("The file was not found.")

else:
    print("File loaded successfully")
    print("Length:", len(content))

# output:
# File loaded successfully
# Length: 67