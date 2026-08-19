try:
    with open("ghost.txt", "r") as f:
        content = f.read()

    print(content)

except FileNotFoundError:
    print("The file was not found.")

# output:
# The file was not found.