with open("DAY_6_EXERCISES/note.txt", "r") as source, open("DAY_6_EXERCISES/notes_upper.txt", "w") as dest:
    for line in source:
        dest.write(line.upper())

"""
Successfuly copied and created new file"""