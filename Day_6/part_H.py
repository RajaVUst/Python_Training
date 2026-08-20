def parse_log(path):
    records = []
    skipped = 0

    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(maxsplit=3)

            try:
                date = parts[0]
                time = parts[1]
                level = parts[2]
                message = parts[3]

                records.append(
                    {
                        "timestamp": f"{date} {time}",
                        "level": level,
                        "message": message,
                    }
                )

            except IndexError:
                skipped += 1

    return records, skipped


logs, skipped = parse_log("access.log")

print("Successfully parsed:", len(logs))
print("Skipped:", skipped)

for log in logs:
    print(log)