logs = [
    "INFO: Application started",
    "INFO: User logged in",
    "WARNING: Low disk space",
    "ERROR: Database timeout",
    "INFO: Application closed"
]
 
with open(r"Day8\refdoc\log.txt", "w") as file:
    for log in logs:
        file.write(log + "\n")
 
with open(r"Day8\refdoc\log.txt", "r") as file:
    for line_no, line in enumerate(file, start=1):
        print(f"{line_no}: {line.strip()}")
 
file = open(r"Day_8\refdoc\log.txt", "r")
 
for line in file:
    print(line.strip())
 
# Forgot:
# file.close()
 
with open("log.txt", "a") as file:
    file.write("INFO: New session started\n")
 
#  Output:
"""
1: INFO: Application started
2: INFO: User logged in
3: WARNING: Low disk space
4: ERROR: Database timeout
5: INFO: Application closed
INFO: Application started
INFO: User logged in
WARNING: Low disk space
ERROR: Database timeout
INFO: Application closed
"""
 