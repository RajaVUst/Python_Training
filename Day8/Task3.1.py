
# Five log lines
logs = [
    "Application started",
    "User logged in",
    "Product searched",
    "Order created",
    "Application closed"
]

# Write the logs to a file
with open("log.txt", "w") as file:
    for log in logs:
        file.write(log + "\n")

# Read the file line by line
with open("log.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())

# Output:
# 1 Application started
# 2 User logged in
# 3 Product searched
# 4 Order created
# 5 Application closed

#Manual open() / close()
file = open("log.txt", "r")

for line in file:
    print(line.strip())

# If we forget:
# file.close()

# Risk:
# Forgetting to close a file can cause a file-handle leak.
# Data may also remain unflushed when writing.

# Correct approach with 'with' statement
with open("log.txt", "r") as file:
    for line in file:
        print(line.strip())

# Output:
# Application started
# User logged in
# Product searched
# Order created
# Application closed

with open("log.txt", "a") as file:
    file.write("New log entry\n")

print("New log added.")

# Output:
# New log added.