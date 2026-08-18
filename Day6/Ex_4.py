with open(r"C:\training\Python_Training\Day_6\Ref doc\notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
 
        if not clean_line:
            continue
 
        print(clean_line.upper())
 
# Output:
# HELLO WORLD
# HELLO PYTHON
 