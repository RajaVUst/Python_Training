with open("day6/notes.txt", "r") as source, open("day6/notes_upper.txt", "w") as destination:
    for line in source:
        destination.write(line.upper())

"""
OUTPUT:
HELLO WORLD!!!
GOOD MORNING
"""