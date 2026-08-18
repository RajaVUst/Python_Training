with open("notes.txt", "r") as source, open("notes_upper.txt", "w") as dest:
    for line in source:
        dest.write(line.upper())

print("notes_upper.txt created successfully.")
