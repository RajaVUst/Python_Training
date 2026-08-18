def parse_log(path):
    logs = []
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

            logs.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })

    return logs, skipped


logs, skipped = parse_log("access.log")

print("Successfully parsed:", len(logs))
print("Skipped:", skipped)

for log in logs:
    print(log)



#output:
'''Successfully parsed: 3
Skipped: 1
{'timestamp': '2023-10-01 10:00:00', 'level': 'INFO', 'message': 'User logged in'}
{'timestamp': '2023-10-01 10:05:00', 'level': 'WARNING', 'message': 'Disk space low'}
{'timestamp': '2023-10-01 10:10:00', 'level': 'ERROR', 'message': 'Failed to connect to database'}'''