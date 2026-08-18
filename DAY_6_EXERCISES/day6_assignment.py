def parse_log(path):
    records = []
    skipped = 0

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            parts = line.split(maxsplit=3)

            if len(parts) < 4:
                skipped += 1
                continue

            date = parts[0]
            time = parts[1]
            level = parts[2]
            message = parts[3]

            records.append({
                "timestamp": f"{date} {time}",
                "level": level,
                "message": message
            })

    return records, skipped

logs, skipped = parse_log("DAY_6_EXERCISES/access.log")

print("Parsed:", len(logs))
print("Skipped:", skipped)

for log in logs:
    print(log)


"""
Output->
Parsed: 7
Skipped: 1
{'timestamp': '2026-03-23 10:00', 'level': 'INFO', 'message': 'Application started'}
{'timestamp': '2026-03-23 10:01', 'level': 'INFO', 'message': 'User login successful'}
{'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout'}
{'timestamp': '2026-03-23 10:03', 'level': 'WARNING', 'message': 'Low disk space'}
{'timestamp': '2026-03-23 10:05', 'level': 'INFO', 'message': 'Settings loaded'}
{'timestamp': '2026-03-23 10:06', 'level': 'ERROR', 'message': 'Database unavailable'}
{'timestamp': '2026-03-23 10:07', 'level': 'INFO', 'message': 'Application stopped'}
"""