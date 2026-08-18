with open("notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        if not clean_line:
            continue
        print(clean_line.upper())
