
try:
    with open("notes.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("notes.txt doesn't exist -- please check the file path.")
else:
    print("File loaded successfully")
    print(len(data))
    
#output
# File loaded successfully
# 259