try:
    with open("notes.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File not found")

else:
    print("File loaded successfully")
    print(len(content))

    # output
    # File loaded successfully
    #  47