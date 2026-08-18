
def parse_log(path):
    entries = []
    skipped = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # date, time, level, message  (maxsplit=3 keeps the message intact)
            parts = line.split(maxsplit=3)
            if len(parts) < 4:
                skipped += 1
                continue
            date, time, level, message = parts
            entries.append({
                "timestamp": f"{date} {time}",
                "level": level,
                "message": message,
            })
    print(f"Parsed {len(entries)} lines successfully, skipped {skipped} malformed line(s)")
    return entries

parsed = parse_log("Day6/access.log")

for entry in parsed:
    print(entry)
    
#output
# Parsed 7 lines successfully, skipped 1 malformed line(s)

# {'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout'}
# {'timestamp': '2026-03-23 10:05', 'level': 'INFO', 'message': 'Server started successfully'}
# {'timestamp': '2026-03-23 10:07', 'level': 'WARNING', 'message': 'Disk usage above 80 percent'}
# {'timestamp': '2026-03-23 10:12', 'level': 'INFO', 'message': 'User login accepted'}
# {'timestamp': '2026-03-23 10:15', 'level': 'DEBUG', 'message': 'Cache refreshed'}
# {'timestamp': '2026-03-23 10:18', 'level': 'WARNING', 'message': 'Slow response from database'}
# {'timestamp': '2026-03-23 10:21', 'level': 'INFO', 'message': 'Backup completed'}