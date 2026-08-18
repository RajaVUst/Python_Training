
with open("notes.txt") as f:
    for line in f:
        clean_line = line.strip()
        if not clean_line:
            continue
        print(clean_line.upper())
#output
# PYTHON IS A VERSATILE PROGRAMMING LANGUAGE.
# IT IS WIDELY USED FOR WEB DEVELOPMENT AND DATA SCIENCE.
# FILE HANDLING LETS PROGRAMS READ AND WRITE DATA ON DISK.
# EXCEPTIONS HELP PROGRAMS HANDLE ERRORS GRACEFULLY.
# PRACTICE IS THE BEST WAY TO MASTER THESE CONCEPTS.