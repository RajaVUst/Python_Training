
try:
    with open("ghost.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("ghost.txt doesn't exist -- please check the file path.")
    
#output
# ghost.txt doesn't exist -- please check the file path.