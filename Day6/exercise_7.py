with open("diary.txt", "a") as f:
    f.write("I learned exceptions.\n")
with open("diary.txt", "r") as f:
    content = f.read()
print(content)

# output
# I learned Python functions.
# I learned lists and dictionaries.
# I learned file handling.
# I learned exceptions.