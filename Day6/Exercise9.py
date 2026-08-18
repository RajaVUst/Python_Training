
with open("notes.txt") as src, open("notes_upper.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())

with open("notes_upper.txt") as f:
    print(f.read())
    
#output
# PYTHON IS A VERSATILE PROGRAMMING LANGUAGE.
# IT IS WIDELY USED FOR WEB DEVELOPMENT AND DATA SCIENCE.
# FILE HANDLING LETS PROGRAMS READ AND WRITE DATA ON DISK.
# EXCEPTIONS HELP PROGRAMS HANDLE ERRORS GRACEFULLY.
# PRACTICE IS THE BEST WAY TO MASTER THESE CONCEPTS.