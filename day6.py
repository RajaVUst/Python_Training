# Q1
with open("notes.txt", "r") as f:
    content = f.read()

print(len(content))

# Q2
with open("notes.txt", "r") as f:
    print(f.readline().strip())

# Q3
with open("notes.txt", "r") as f:
    lines = f.readlines()

print(len(lines))
print(lines)

# Q4
with open("notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()

        if not clean_line:
            continue

        print(clean_line.upper())

# Q5
word_count = 0

with open("notes.txt", "r") as f:
    for line in f:
        word_count += len(line.split())

print(word_count)

# Q6
with open("diary.txt", "w") as f:
    f.write("Learned Python functions\n")
    f.write("Learned file handling\n")
    f.write("Learned exception handling\n")

# Q7
with open("diary.txt", "a") as f:
    f.write("Learned CSV and JSON\n")

with open("diary.txt", "r") as f:
    print(f.read())

# Q8
with open("squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i ** 2) + "\n")

total = 0

with open("squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print(total)

# Q9
with open("notes.txt", "r") as source, open("notes_upper.txt", "w") as target:
    for line in source:
        target.write(line.upper())

# Q10
import csv

with open("scores.csv", "r") as f:
    reader = csv.reader(f)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# Q11
import csv

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['score']}")

# Q12
import csv

scores = []

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

print(sum(scores) / len(scores))

# Q13
import csv

students = [
    ["Reni", 90],
    ["Asha", 85],
    ["Rahul", 78],
    ["Anu", 95]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "score"])

    for student in students:
        writer.writerow(student)

# Q14
import json

with open("profile.json", "r") as f:
    profile = json.load(f)

print(profile["name"])
print(len(profile["completed_days"]))

# Q15
import json

with open("profile.json", "r") as f:
    profile = json.load(f)

profile["completed_days"].append(6)

with open("profile.json", "w") as f:
    json.dump(profile, f, indent=2)

# Q16
import json

session = {
    "topic": "File Handling",
    "duration_minutes": 60,
    "format": "Practice Lab"
}

json_string = json.dumps(session)

print(json_string)

data = json.loads(json_string)

print(type(data))

# Q17
import csv
import json

records = []

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        records.append(dict(row))

with open("scores.json", "w") as f:
    json.dump(records, f, indent=2)

# Q18
try:
    with open("ghost.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("File not found.")

# Q19
value = "abc"

try:
    num = int(value)
    print(num)

except ValueError:
    print("Invalid number.")

# Q20
num1 = "10"
num2 = "0"

try:
    result = int(num1) / int(num2)
    print(result)

except ValueError:
    print("Invalid numeric input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# Q21
try:
    with open("notes.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("File not found.")

else:
    print("File loaded successfully")
    print(len(content))

# Q22
try:
    with open("notes.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Attempt finished")

# Q23
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return age

try:
    print(check_age(25))
    print(check_age(-5))

except ValueError as e:
    print(e)

# Q24
class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")

    return score

# Q25
test_scores = [80, -10, 50, 150, 95]

for score in test_scores:
    try:
        print(validate_score(score))

    except InvalidScoreError as e:
        print(e)

# Q26
import csv

def load_scores(path):
    scores = {}

    try:
        with open(path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    scores[row["name"]] = int(row["score"])

                except (ValueError, TypeError):
                    continue

    except FileNotFoundError:
        return {}

    return scores

print(load_scores("scores.csv"))

# Q27
def summarise(scores):
    return {
        "count": len(scores),
        "average": sum(scores.values()) / len(scores),
        "highest": max(scores.values()),
        "lowest": min(scores.values())
    }

sample_scores = {
    "Asha": 80,
    "Ravi": 90,
    "Renu": 70
}

print(summarise(sample_scores))

# Q28
def word_frequencies(path):
    frequencies = {}

    with open(path, "r") as f:
        words = f.read().lower().split()

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies

print(word_frequencies("notes.txt"))

# Q29
import json

class MissingConfigKeyError(Exception):
    pass

def load_config(path):
    with open(path, "r") as f:
        data = json.load(f)

    if "batch_size" not in data:
        raise MissingConfigKeyError("batch_size missing")

    if "learning_rate" not in data:
        raise MissingConfigKeyError("learning_rate missing")

    return data

try:
    config = load_config("config.json")
    print(config)

except MissingConfigKeyError as e:
    print(e)

# Q30
def parse_log(path):
    logs = []
    skipped = 0

    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=3)

            if len(parts) < 4:
                skipped += 1
                continue

            logs.append({
                "timestamp": f"{parts[0]} {parts[1]}",
                "level": parts[2],
                "message": parts[3]
            })

    print("Parsed:", len(logs)