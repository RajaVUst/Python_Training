with open("notes.txt", "r") as source:
    with open("notes_upper.txt", "w") as destination:
        for line in source:
            destination.write(line.upper())