# Copy and transform a file
with open("Day6/notes.txt", "r") as source:
    with open("Day6/notes_upper.txt", "w") as destination:

        for line in source:
            destination.write(line.upper())