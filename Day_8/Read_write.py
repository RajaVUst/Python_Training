log_lines = [
    "System started",
    "User logged in",
    "Data loaded",
    "Report generated",
    "System shutdown"
]
with open("log.txt", "w") as file:
    for line in log_lines:
        file.write(line + "\n")
with open("log.txt", "r") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}. {line.strip()}")
file = open("log.txt", "a")
file.write("Manual open example\n")
with open("log.txt", "a") as file:
    file.write("Append mode example\n")
print()
#  Output:
# 1. System started
# 2. User logged in
# 3. Data loaded
# 4. Report generated
# 5. System shutdown

