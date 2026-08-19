with open("notes.txt", "r") as f:
    lines = f.readlines()

print(len(lines))
print(lines)

# output:
# 3
# ['Hey there\n', 'I am Chandrashekhar \n', 'And this is the 6th day of training\n']