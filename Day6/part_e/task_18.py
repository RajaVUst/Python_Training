try:
    with open("ghost.txt", "r") as f:
        content = f.read()

    print(content)

except FileNotFoundError:
    print("The file was not found.")


# The file was not found.