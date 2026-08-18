def parse_log(path):
    parsed_logs = []
    skipped = 0
 
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=3)
 
            if len(parts) < 4:
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
 
 
logs, skipped = parse_log(
    r"C:\training\Python_Training\Day_6\Ref doc\access.log"
)
 
print("Successfully parsed:", len(logs))
print("Skipped:", skipped)
 
for log in logs:
    print(log)
 
# Output:
"""
Successfully parsed: 5
Skipped: 2
{'timestamp': '2023-01-01 12:00:00', 'level': 'INFO', 'message': 'User logged in'}
{'timestamp': '2023-01-01 12:05:00', 'level': 'WARNING', 'message': 'Low disk space'}
{'timestamp': '2023-01-01 12:10:00', 'level': 'ERROR', 'message': 'Failed to connect to database'}
{'timestamp': '2023-01-01 12:15:00', 'level': 'INFO', 'message': 'Backup completed successfully'}
{'timestamp': '2023-01-01 12:20:00', 'level': 'DEBUG', 'message': 'Variable values initialized'}
"""
 