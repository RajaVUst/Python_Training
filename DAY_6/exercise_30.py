def parse_log(path):
    parsed = []
    skipped = 0

    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=2)
            if len(parts) < 3:
                skipped += 1
                continue
            parsed.append({
                "timestamp": parts[0] + " " + parts[1],
                "level":     parts[1],
                "message":   parts[2],
            })

    print(f"Parsed: {len(parsed)} lines, Skipped: {skipped} lines")
    return parsed

logs = parse_log("access.log")
for entry in logs:
    print(entry)
