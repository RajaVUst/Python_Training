with open(r"Day_6\Ref doc\notes.txt", "r") as source, \
    open(r"Day_6\Ref doc\notes_upper.txt", "w") as destination:

    for line in source:
        destination.write(line.upper())

print("notes_upper.txt created successfully!")

# Output:
# notes_upper.txt created successfully!
