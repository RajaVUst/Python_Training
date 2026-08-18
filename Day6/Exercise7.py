
with open("diary.txt", "a") as f:
    f.write("I learned to iterate over a file object directly with a for loop.\n")

with open("diary.txt") as f:
    print(f.read())
    
#output
# I learned how to read files with with open().
# I learned the difference between read(), readline(), and readlines().
# I learned that mode 'w' overwrites while mode 'a' appends.
# I learned to iterate over a file object directly with a for loop.