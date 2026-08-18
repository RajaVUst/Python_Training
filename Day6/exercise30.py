# Day 6 - Exercise 30


# for creating and writing log file and data
# log_lines = [
#     "2026-03-23 10:02 ERROR Connection timeout\n",
#     "2026-03-23 10:05 INFO User logged in\n",
#     "2026-03-23 10:07 WARNING Disk space is low\n",
#     "Malformed line\n",
#     "2026-03-23 10:10 INFO File uploaded successfully\n",
#     "2026-03-23 10:12 ERROR Database unavailable\n",
#     "2026-03-23 10:15 DEBUG Request received\n"
# ]
#
# with open("access.log", "w") as f:
#     f.writelines(log_lines)


def parse_log(path):
    parsed_logs = []
    skipped_count = 0
    valid_levels = {"INFO", "WARNING", "ERROR", "DEBUG"}

    try:
        with open(path, "r") as f:
            for line in f:
                parts = line.strip().split(maxsplit=3)

                if len(parts) != 4:
                    skipped_count += 1
                    continue

                date, time, level, message = parts

                if level not in valid_levels:
                    skipped_count += 1
                    continue

                parsed_logs.append({
                    "timestamp": f"{date} {time}",
                    "level": level,
                    "message": message
                })

    except FileNotFoundError:
        print(f"{path} was not found.")
        return [], 0

    return parsed_logs, skipped_count


logs, skipped = parse_log("access.log")

print("Parsed successfully:", len(logs))
print("Skipped:", skipped)

for log in logs:
    print(log)


#output
'''
Parsed successfully: 6
Skipped: 1
{'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout'}
{'timestamp': '2026-03-23 10:05', 'level': 'INFO', 'message': 'User logged in'}
{'timestamp': '2026-03-23 10:07', 'level': 'WARNING', 'message': 'Disk space is low'}
{'timestamp': '2026-03-23 10:10', 'level': 'INFO', 'message': 'File uploaded successfully'}
{'timestamp': '2026-03-23 10:12', 'level': 'ERROR', 'message': 'Database unavailable'}
{'timestamp': '2026-03-23 10:15', 'level': 'DEBUG', 'message': 'Request received'}
'''
