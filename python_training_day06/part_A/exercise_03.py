with open("notes.txt", "r") as f:
    lines = f.readlines()

print(len(lines))
print(lines)


#output:  5 ['Python is easy to learn.\n', 'I am practicing file handling.\n', 'Today I learned about exceptions.\n', 'I want to improve my Python skills.\n', 'Practice makes programming easier.\n']