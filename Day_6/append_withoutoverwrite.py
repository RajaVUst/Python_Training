with open("diary.txt", "a") as f:
    f.write("I practiced reading and writing JSON files.\n")

with open("diary.txt", "r") as f:
    content = f.read()

print(content)