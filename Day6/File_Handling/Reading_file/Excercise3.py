# Read all lines into a list

with open("Day6/notes.txt", "r") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))
print(lines)

# Output:
# Number of lines: 2
# ['Hello!\n', 'I am learning python\n']