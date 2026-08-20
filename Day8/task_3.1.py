log_lines = [
    "Application started",
    "User logged in",
    "Data loaded successfully",
    "User updated profile",
    "Application closed"
]


#  5 log lines using "w" mode and with block

with open("log.txt", "w") as file:
    for line in log_lines:
        file.write(line + "\n")


#  Read the file line by line and print line numbers

with open("log.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")


#  Manual open() / close()

file = open("log.txt", "r")

for line in file:
    print(line.strip())

file.close()


#  Deliberately forget to close the file

file = open("log.txt", "r")

for line in file:
    print(line.strip())

# file.close() is intentionally missing.
#
# Risk:
# Forgetting to close a file can cause a file handle leak.
# When writing, it can also leave buffered data unflushed.
# Therefore, using "with open()" is recommended.


#   using with

with open("log.txt", "r") as file:
    for line in file:
        print(line.strip())


#  Append mode "a"

with open("log.txt", "a") as file:
    file.write("New log entry added\n")
    file.write("Another log entry added\n")

# "a" appends data to the existing file.
# It does not overwrite the existing contents.




# 1: Application started
# 2: User logged in
# 3: Data loaded successfully
# 4: User updated profile
# 5: Application closed
# Application started
# User logged in
# Data loaded successfully
# User updated profile
# Application closed
# Application started
# User logged in
# Data loaded successfully
# User updated profile
# Application closed
# Application started
# User logged in
# Data loaded successfully
# User updated profile
# Application closed