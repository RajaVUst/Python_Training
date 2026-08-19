with open("oneline.txt", "r") as f:
    for line in f:
        clean_line = line.strip()

        if not clean_line:
            continue

        print(clean_line.upper())
        
# OUTPUT
# HELLO
# I
# AM
# BONNY