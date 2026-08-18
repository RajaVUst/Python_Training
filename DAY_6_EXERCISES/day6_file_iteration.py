with open("DAY_6_EXERCISES/note.txt", "r") as f:
    for line in f:
        clear_line = line.strip()

        if not clear_line:
            continue

        print(clear_line.upper())

"""
Output->
HELLO FROM NOTES FILE.
PYTHON FILE HANDLING IS USEFUL.
THIS IS THE THIRD LINE.
PRACTICE MAKES CODING EASIER.
END OF SAMPLE NOTES.
"""
