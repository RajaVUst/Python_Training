# Exercise 30: Draft a Mini Log Parser

# Create access.log

with open("access.log", "w") as f:
    f.write("2026-03-23 10:02 ERROR Connection timeout\n")
    f.write("2026-03-23 10:05 INFO User login successful\n")
    f.write("2026-03-23 10:10 WARNING Low disk space\n")
    f.write("Malformed line\n")
    f.write("2026-03-23 10:15 ERROR Database unavailable\n")
    f.write("2026-03-23 10:20 INFO File uploaded\n")
    f.write("2026-03-23 10:25 WARNING High memory usage\n")
    f.write("2026-03-23 10:30 INFO Logout successful\n")


def parse_log(path):
    logs = []
    skipped = 0

    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=2)

            if len(parts) < 3:
                skipped += 1
                continue

            logs.append({
                "timestamp": f"{parts[0]} {parts[1]}",
                "level": parts[2].split(maxsplit=1)[0],
                "message": parts[2][len(parts[2].split(maxsplit=1)[0]):].strip()
            })

    return logs, skipped


parsed_logs, skipped_count = parse_log("access.log")

print("Parsed Successfully:", len(parsed_logs))
print("Skipped Lines:", skipped_count)
print(parsed_logs)

# Output:
# Parsed Successfully: 7
# Skipped Lines: 1
#
# [
#   {
#     'timestamp': '2026-03-23 10:02',
#     'level': 'ERROR',
#     'message': 'Connection timeout'
#   },
#   {
#     'timestamp': '2026-03-23 10:05',
#     'level': 'INFO',
#     'message': 'User login successful'
#   },
#   {
#     'timestamp': '2026-03-23 10:10',
#     'level': 'WARNING',
#     'message': 'Low disk space'
#   },
#   {
#     'timestamp': '2026-03-23 10:15',
#     'level': 'ERROR',
#     'message': 'Database unavailable'
#   },
#   {
#     'timestamp': '2026-03-23 10:20',
#     'level': 'INFO',
#     'message': 'File uploaded'
#   },
#   {
#     'timestamp': '2026-03-23 10:25',
#     'level': 'WARNING',
#     'message': 'High memory usage'
#   },
#   {
#     'timestamp': '2026-03-23 10:30',
#     'level': 'INFO',
#     'message': 'Logout successful'
#   }
# ]