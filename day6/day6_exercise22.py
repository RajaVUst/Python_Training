try:
    with open("day6/notes.txt", "r") as f:
        content = f.read()
        print("Read successful.")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Attempt finished")


try:
    with open("day6/ghost.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File not found.")

finally:
    print("Attempt finished")

"""
OUTPUT:
Read successful.
Attempt finished
File not found.
Attempt finished
"""