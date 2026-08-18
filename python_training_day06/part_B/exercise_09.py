with open("../part_A/notes.txt", "r") as source:
    with open("notes_upper.txt", "w") as destination:
        for line in source:
            destination.write(line.upper())