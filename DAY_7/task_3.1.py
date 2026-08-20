import os

log_lines = [
    "INFO  2026-08-20 09:00:01 Server started",
    "INFO  2026-08-20 09:00:05 Connection accepted from 192.168.1.10",
    "WARN  2026-08-20 09:01:12 Disk usage above 80%",
    "ERROR 2026-08-20 09:02:34 Failed to read config file",
    "INFO  2026-08-20 09:03:00 Scheduled backup completed",
]

log_path = os.path.join(os.path.dirname(__file__), "log.txt")

# Write using with block (safe — file is closed automatically on exit)
with open(log_path, "w") as f:
    for line in log_lines:
        f.write(line + "\n")

# Read back line by line with line numbers
print("--- Reading log.txt ---")
with open(log_path, "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line}", end="")

# Without with: manual open/close
# f = open(log_path, "r")
# data = f.read()
# (if we forget f.close() here the OS file handle stays open until the
#  process exits; on Windows this can even block other processes from
#  writing the file, and buffered writes may never reach disk)
# f.close()

# Append a new log entry
print("\n--- Appending to log.txt ---")
with open(log_path, "a") as f:
    f.write("INFO  2026-08-20 09:05:00 Append mode test\n")

with open(log_path, "r") as f:
    print(f.read())
