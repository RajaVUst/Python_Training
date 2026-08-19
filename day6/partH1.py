def parse_log(path):
    records = []
    skipped = 0
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=2)
            if len(parts) != 3:
                skipped += 1
                continue
            timestamp, level, message = parts
            records.append(
                {"timestamp": timestamp, "level": level, "message": message}
            )
    return records, skipped


with open("access.log", "w") as f:
    f.write("2026-03-23T10:02 ERROR Connection timeout\n")
    f.write("2026-03-23T10:05 INFO Server started\n")
    f.write("malformed\n")
    f.write("2026-03-23T10:08 WARNING Memory usage is high\n")
    f.write("2026-03-23T10:10 INFO User logged in\n")
    f.write("2026-03-23T10:12 ERROR Database unavailable\n")
    f.write("2026-03-23T10:15 INFO Request completed\n")

parsed_lines, skipped_lines = parse_log("access.log")
print("Parsed successfully:", len(parsed_lines))
print("Skipped:", skipped_lines)
print(parsed_lines)

# OUTPUT

# Parsed successfully: 6
# Skipped: 1
# [{'timestamp': '2026-03-23T10:02', 'level': 'ERROR', 'message': 'Connection timeout'}, {'timestamp': '2026-03-23T10:05', 'level': 'INFO', 'message': 'Server started'}, {'timestamp': '2026-03-23T10:08', 'level': 'WARNING', 'message': 'Memory usage is high'}, {'timestamp': '2026-03-23T10:10', 'level': 'INFO', 'message': 'User logged in'}, {'timestamp': '2026-03-23T10:12', 'level': 'ERROR', 'message': 'Database unavailable'}, {'timestamp': '2026-03-23T10:15', 'level': 'INFO', 'message': 'Request completed'}]
