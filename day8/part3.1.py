with open("log.txt", "w") as f:
    f.write("Hello.\n")
    f.write("This.\n")
    f.write("is.\n")
    f.write("going.\n")
    f.write("backward.\n")
        
f.close()

with open("log.txt","r") as f:
   lines=f.readlines()
   
for line in reversed(lines):
       print( line.strip())

# OUTPUT

# backward.
# going.
# is.
# This.
# Hello.

f = open("log.txt", "w")

f.write("Hello.\n")
f.write("This file may not be closed properly.\n")

# f.close() is intentionally missing

with open("log.txt", "a") as f:
    f.write("This line is appended.\n")