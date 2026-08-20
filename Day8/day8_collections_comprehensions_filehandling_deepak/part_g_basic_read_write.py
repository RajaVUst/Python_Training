log_lines = ["Server started\n", "User alice logged in\n", "Processed 42 records\n",
             "Warning: low disk space\n", "Server shutting down\n"]

with open("log.txt", "w") as f:
    f.writelines(log_lines)

with open("log.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.rstrip()}")

# manual open without close (deliberately bad)
bad_file = open("log.txt", "r")
print(bad_file.readline().rstrip())
bad_file.close()   # normally "forgotten" -> file handle leak / unflushed buffer risk

with open("log.txt", "a") as f:
    f.write("Additional entry appended after restart\n")

with open("log.txt", "r") as f:
    print(f.read())
# Output:
# 1: Server started
# 2: User alice logged in
# 3: Processed 42 records
# 4: Warning: low disk space
# 5: Server shutting down
# Server started
# Server started
# User alice logged in
# Processed 42 records
# Warning: low disk space
# Server shutting down
# Additional entry appended after restart