def parse_log(path):
    logs = []
    skipped = 0
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=2)
            if len(parts) != 3:
                skipped += 1
                continue
            timestamp = parts[0] + " " + parts[1]
            level = parts[2].split()[0]
            message = " ".join(parts[2].split()[1:])
            logs.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })
    return logs, skipped
logs, skipped = parse_log("access.log")
print("Parsed:", len(logs))
print("Skipped:", skipped)
print(logs)

# output
# Parsed: 5
# Skipped: 1
# [{'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout'}, {'timestamp': '2026-03-23 10:05', 'level': 'INFO', 'message': 'User logged in'}, {'timestamp': '2026-03-23 10:10', 'level': 'WARNING', 'message': 'Low disk space'}, {'timestamp': '2026-03-23 10:15', 'level': 'ERROR', 'message': 'Database failed'}, {'timestamp': '2026-03-23 10:20', 'level': 'INFO', 'message': 'Request completed'}]