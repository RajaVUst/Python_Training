with open("notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()

        if not clean_line:
            continue

        print(clean_line.upper())



#output:
''' I AM PRACTICING FILE HANDLING.
TODAY I LEARNED ABOUT EXCEPTIONS.
I WANT TO IMPROVE MY PYTHON SKILLS.
PRACTICE MAKES PROGRAMMING EASIER. '''
