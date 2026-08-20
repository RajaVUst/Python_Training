log_lines = [
    "Application started",
    "User logged in",
    "File uploaded",
    "Report generated",
    "Application stopped"
]

# Write using a with block
with open("log.txt", "w", encoding="utf-8") as file:
    for line in log_lines:
        file.write(line + "\n")


# Read line by line
with open("log.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")


# Manual file handling
manual_file = open(
    "manual_example.txt",
    "w",
    encoding="utf-8"
)

manual_file.write("This file was opened manually.\n")

# Forgetting close() may cause a file-handle leak or leave buffered data unwritten.
manual_file.close()


# Append without overwriting
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("A new log entry was appended\n")


print("\nAfter appending:")

with open("log.txt", "r", encoding="utf-8") as file:
    print(file.read())

#output
'''
1: Application started
2: User logged in
3: File uploaded
4: Report generated
5: Application stopped

After appending:
Application started
User logged in
File uploaded
Report generated
Application stopped

'''
