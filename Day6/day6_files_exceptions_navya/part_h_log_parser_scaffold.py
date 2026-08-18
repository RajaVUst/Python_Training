# Exercise 30 - Draft a mini log parser
def parse_log(path):
    parsed_logs = []
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

            timestamp = parts[0] + " " + parts[1]
            level = parts[2]
            message = parts[3]

            parsed_logs.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })

    print(f"Parsed successfully: {len(parsed_logs)}")
    print(f"Skipped: {skipped_count}")
    return parsed_logs

logs = parse_log("access.log")
print(logs)
# Output:
# Parsed successfully: 7
# Skipped: 1
# [{'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout'}, {'timestamp': '2026-03-23 10:05', 'level': 'INFO', 'message': 'Server started successfully'}, {'timestamp': '2026-03-23 10:07', 'level': 'WARNING', 'message': 'High memory usage detected'}, {'timestamp': '2026-03-23 10:10', 'level': 'ERROR', 'message': 'Database connection failed'}, {'timestamp': '2026-03-23 10:15', 'level': 'INFO', 'message': 'Backup completed'}, {'timestamp': '2026-03-23 10:18', 'level': 'WARNING', 'message': 'Disk space low'}, {'timestamp': '2026-03-23 10:20', 'level': 'ERROR', 'message': 'Timeout on request'}]