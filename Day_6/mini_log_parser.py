def parse_log(path):
    parsed_logs = []
    skipped = 0

    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=3)

            if len(parts) != 4:
                skipped += 1
                continue

            timestamp = parts[0] + " " + parts[1]
            level = parts[2]
            message = parts[3]

            parsed_logs.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })

    return parsed_logs, skipped


logs, skipped = parse_log("access.log")

print("Successfully parsed:", len(logs))
print("Skipped:", skipped)

for log in logs:
    print(log)

# output:
# Successfully parsed: 6
# Skipped: 1
# {'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout'}
# {'timestamp': '2026-03-23 10:05', 'level': 'INFO', 'message': 'User logged in'}
# {'timestamp': '2026-03-23 10:08', 'level': 'WARNING', 'message': 'Disk space low'}
# {'timestamp': '2026-03-23 10:10', 'level': 'ERROR', 'message': 'Database unavailable'}
# {'timestamp': '2026-03-23 10:15', 'level': 'INFO', 'message': 'File uploaded'}
# {'timestamp': '2026-03-23 10:20', 'level': 'INFO', 'message': 'User logged out'}