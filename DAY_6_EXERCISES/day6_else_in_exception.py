try:
    with open("DAY_6_EXERCISES/note.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File not found.")

else:
    print("File loaded successfully")
    print("Length:", len(content))

"""
Output->
File loaded successfully
Length: 129
"""