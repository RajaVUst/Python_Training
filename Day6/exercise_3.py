with open("notes.txt", "r") as f:
    lines = f.readlines()
print(len(lines))
print(lines)

# output
# 3
# ['Hello World\n', 'I am learning Python\n', 'Today is Day 6']