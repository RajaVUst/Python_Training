try:
    with open("note.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Attempt finished")

"""
Output->
File not found.
Attempt finished
"""