def parse_log(path):
    entries = []
    skipped = 0

    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=3)

            if len(parts) < 4:
                skipped += 1
                continue

            date, time, level, message = parts

            entries.append({
                "timestamp": f"{date} {time}",
                "level": level,
                "message": message
            })

    return entries, skipped

parsed_logs, skipped_count = parse_log("day6/access.log")

print("Successfully parsed:", len(parsed_logs))
print("Skipped:", skipped_count)

print("\nParsed Entries:")
for entry in parsed_logs:
    print(entry)

"""
OUTPUT:
Successfully parsed: 8
Skipped: 0

Parsed Entries:
{'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout\\n")'}
{'timestamp': 'f.write("2026-03-23 10:05', 'level': 'INFO', 'message': 'User login successful\\n")'}
{'timestamp': 'f.write("2026-03-23 10:07', 'level': 'WARNING', 'message': 'Disk space low\\n")'}
{'timestamp': 'f.write("2026-03-23 10:10', 'level': 'INFO', 'message': 'File uploaded\\n")'}
{'timestamp': 'f.write("MALFORMED LINE\\n")', 'level': '#', 'message': 'Missing fields'}
{'timestamp': 'f.write("2026-03-23 10:15', 'level': 'ERROR', 'message': 'Database unavailable\\n")'}
{'timestamp': 'f.write("2026-03-23 10:18', 'level': 'INFO', 'message': 'Password changed\\n")'}
{'timestamp': 'f.write("2026-03-23 10:20', 'level': 'WARNING', 'message': 'High memory usage\\n")'}
"""