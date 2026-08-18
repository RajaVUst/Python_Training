# Exercise 30 - Draft a mini log parser
log_lines = [
    "2026-03-23 10:02 ERROR Connection timeout\n",
    "2026-03-23 10:03 INFO Server started successfully\n",
    "2026-03-23 10:05 WARNING Disk space running low\n",
    "2026-03-23 10:07 INFO User logged in\n",
    "2026-03-23 10:09 ERROR Database connection failed\n",
    "2026-03-23 10:10 INFO Backup completed\n",
    "MALFORMED LINE\n",
    "2026-03-23 10:15 WARNING\n",
]
with open("access.log", "w") as f:
    f.writelines(log_lines)

def parse_log(path):
    parsed_entries = []
    skipped_count = 0
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(maxsplit=3)
            if len(parts) < 4:
                skipped_count += 1
                continue
            date, time, level, message = parts
            parsed_entries.append({"timestamp": f"{date} {time}", "level": level, "message": message})
    print(f"Parsed successfully: {len(parsed_entries)}")
    print(f"Skipped (malformed): {skipped_count}")
    return parsed_entries

entries = parse_log("access.log")
for entry in entries:
    print(entry)
# Output:
# Parsed successfully: 6
# Skipped (malformed): 2
# {'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout'}
# {'timestamp': '2026-03-23 10:03', 'level': 'INFO', 'message': 'Server started successfully'}
# {'timestamp': '2026-03-23 10:05', 'level': 'WARNING', 'message': 'Disk space running low'}
# {'timestamp': '2026-03-23 10:07', 'level': 'INFO', 'message': 'User logged in'}
# {'timestamp': '2026-03-23 10:09', 'level': 'ERROR', 'message': 'Database connection failed'}
# {'timestamp': '2026-03-23 10:10', 'level': 'INFO', 'message': 'Backup completed'}