with open("diary.txt", "a") as f:
    f.write("I learned how to append to a file without overwriting it.\n")

with open("diary.txt", "r") as f:
    print(f.read())
