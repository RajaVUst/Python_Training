# Catch a missing file

try:
    with open("ghost.txt", "r") as f:
        data = f.read()
    print(data)

except FileNotFoundError:
    print("File not found.")


# Output:
# File not found.