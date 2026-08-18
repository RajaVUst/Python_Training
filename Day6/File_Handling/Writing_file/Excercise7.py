# Append without overwriting

with open("Day6/diary.txt", "a") as f:
    f.write("I learned JSON files.\n")

with open("Day6/diary.txt", "r") as f:
    data = f.read()

print(data)


#Output:
# I learned Python files.
# I learned CSV files.
# I learned exceptions.
# I learned JSON files.
# I learned JSON files.