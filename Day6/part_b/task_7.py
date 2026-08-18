with open("diary.txt", "a") as f:
    f.write("I learned how to append data without deleting existing content.\n")

with open("diary.txt", "r") as f:
    content = f.read()

print(content)