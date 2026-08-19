"""
Day 6 — Files, CSV, JSON, and Exceptions
All 30 exercises with real, verified output shown as comments
right after each block. Run this file top to bottom; it creates
every file it needs (notes.txt, diary.txt, scores.csv, etc.) as it goes.
"""

import csv
import json


# -----------------------------------------------------------------
# Setup: notes.txt (4-5 lines, includes one blank line on purpose
# so Exercise 4's blank-line skip actually has something to skip)
# -----------------------------------------------------------------
with open("notes.txt", "w") as f:
    f.write("Python is fun to learn.\n")
    f.write("Files can be read line by line.\n")
    f.write("\n")
    f.write("CSV and JSON are common data formats.\n")
    f.write("Exceptions keep programs from crashing.\n")


# ===================================================================
# PART A: Reading Files
# ===================================================================

# --- Exercise 1: Read the whole file ---
with open("notes.txt") as f:
    content = f.read()
print("Length in characters:", len(content))
# Output:
# Length in characters: 135


# --- Exercise 2: Read just the first line ---
with open("notes.txt") as f:
    first_line = f.readline().strip()
print("First line:", first_line)
# Output:
# First line: Python is fun to learn.


# --- Exercise 3: Read all lines into a list ---
with open("notes.txt") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))
print("Lines list:", lines)
# Output:
# Number of lines: 5
# Lines list: ['Python is fun to learn.\n', 'Files can be read line by line.\n',
#              '\n', 'CSV and JSON are common data formats.\n',
#              'Exceptions keep programs from crashing.\n']


# --- Exercise 4: Line-by-line iteration, skip blanks, print upper ---
with open("notes.txt") as f:
    for line in f:
        clean_line = line.strip()
        if not clean_line:
            continue
        print(clean_line.upper())
# Output:
# PYTHON IS FUN TO LEARN.
# FILES CAN BE READ LINE BY LINE.
# CSV AND JSON ARE COMMON DATA FORMATS.
# EXCEPTIONS KEEP PROGRAMS FROM CRASHING.


# --- Exercise 5: Count words in a file ---
with open("notes.txt") as f:
    total_words = 0
    for line in f:
        total_words += len(line.split())
print("Total words:", total_words)
# Output:
# Total words: 24


# ===================================================================
# PART B: Writing & Appending Files
# ===================================================================

# --- Exercise 6: Write a fresh file ---
with open("diary.txt", "w") as f:
    f.write("I learned how to open and close files with 'with'.\n")
    f.write("I learned the difference between read() and readlines().\n")
    f.write("I learned that 'w' mode overwrites a file.\n")
print("diary.txt created with 3 lines.")
# Output:
# diary.txt created with 3 lines.


# --- Exercise 7: Append without overwriting ---
with open("diary.txt", "a") as f:
    f.write("I learned that 'a' mode appends instead of overwriting.\n")

with open("diary.txt") as f:
    print(f.read())
# Output:
# I learned how to open and close files with 'with'.
# I learned the difference between read() and readlines().
# I learned that 'w' mode overwrites a file.
# I learned that 'a' mode appends instead of overwriting.


# --- Exercise 8: Write squares of 1-10, read back, sum ---
with open("squares.txt", "w") as f:
    for n in range(1, 11):
        f.write(str(n * n) + "\n")

total = 0
with open("squares.txt") as f:
    for line in f:
        total += int(line.strip())
print("Sum of squares 1-10:", total)
# Output:
# Sum of squares 1-10: 385


# --- Exercise 9: Copy and uppercase notes.txt -> notes_upper.txt ---
with open("notes.txt") as src, open("notes_upper.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())

with open("notes_upper.txt") as f:
    print(f.read())
# Output:
# PYTHON IS FUN TO LEARN.
# FILES CAN BE READ LINE BY LINE.
#
# CSV AND JSON ARE COMMON DATA FORMATS.
# EXCEPTIONS KEEP PROGRAMS FROM CRASHING.


# ===================================================================
# PART C: Working with .csv Files
# ===================================================================

# Setup: scores.csv — Ravi (105) and Karan (-5) are out of 0-100
# range on purpose, Meera's score is blank on purpose.
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Asha", "88"])
    writer.writerow(["Ravi", "105"])
    writer.writerow(["Meera", ""])
    writer.writerow(["Karan", "-5"])
    writer.writerow(["Divya", "76"])


# --- Exercise 10: Read a CSV with csv.reader ---
with open("scores.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print("Row:", row)
# Output:
# Header: ['name', 'score']
# Row: ['Asha', '88']
# Row: ['Ravi', '105']
# Row: ['Meera', '']
# Row: ['Karan', '-5']
# Row: ['Divya', '76']


# --- Exercise 11: Read a CSV with DictReader ---
with open("scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['score']}")
# Output:
# Asha: 88
# Ravi: 105
# Meera:
# Karan: -5
# Divya: 76


# --- Exercise 12: Compute an average from CSV data ---
valid_scores = []
with open("scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["score"] != "":
            valid_scores.append(int(row["score"]))
        else:
            print(f"Skipping {row['name']}: blank score")
average = sum(valid_scores) / len(valid_scores)
print("Valid scores:", valid_scores)
print("Average:", round(average, 2))
# Output:
# Skipping Meera: blank score
# Valid scores: [88, 105, -5, 76]
# Average: 66.0


# --- Exercise 13: Write a CSV file ---
students = [
    ["Anil", 91],
    ["Bhavana", 67],
    ["Chetan", 84],
    ["Deepa", 73],
]
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(students)

with open("results.csv") as f:
    print(f.read())
# Output:
# name,score
# Anil,91
# Bhavana,67
# Chetan,84
# Deepa,73


# ===================================================================
# PART D: Working with .json Files
# ===================================================================

# Setup: profile.json
profile_data = {
    "name": "Asha",
    "track": "Python Readiness",
    "completed_days": [1, 2, 3, 4, 5],
}
with open("profile.json", "w") as f:
    json.dump(profile_data, f, indent=2)


# --- Exercise 14: Read a JSON file ---
with open("profile.json") as f:
    profile = json.load(f)
print("Name:", profile["name"])
print("Completed days count:", len(profile["completed_days"]))
# Output:
# Name: Asha
# Completed days count: 5


# --- Exercise 15: Modify and re-save JSON ---
with open("profile.json") as f:
    profile = json.load(f)

profile["completed_days"].append(6)

with open("profile.json", "w") as f:
    json.dump(profile, f, indent=2)

with open("profile.json") as f:
    print(f.read())
# Output:
# {
#   "name": "Asha",
#   "track": "Python Readiness",
#   "completed_days": [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6
#   ]
# }


# --- Exercise 16: String <-> JSON with loads/dumps ---
session = {
    "topic": "Files, CSV, JSON, Exceptions",
    "duration_minutes": 90,
    "format": "self-paced exercises",
}
session_str = json.dumps(session)
print("JSON string:", session_str)

session_back = json.loads(session_str)
print("Type after loads():", type(session_back))
# Output:
# JSON string: {"topic": "Files, CSV, JSON, Exceptions", "duration_minutes": 90, "format": "self-paced exercises"}
# Type after loads(): <class 'dict'>


# --- Exercise 17: CSV to JSON ---
rows_as_dicts = []
with open("scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows_as_dicts.append(dict(row))

with open("scores.json", "w") as f:
    json.dump(rows_as_dicts, f, indent=2)

with open("scores.json") as f:
    print(f.read())
# Output:
# [
#   { "name": "Asha", "score": "88" },
#   { "name": "Ravi", "score": "105" },
#   { "name": "Meera", "score": "" },
#   { "name": "Karan", "score": "-5" },
#   { "name": "Divya", "score": "76" }
# ]


# ===================================================================
# PART E: try / except / else / finally
# ===================================================================

# --- Exercise 18: Catch a missing file ---
try:
    with open("ghost.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Oops! 'ghost.txt' does not exist.")
# Output:
# Oops! 'ghost.txt' does not exist.


# --- Exercise 19: Catch a bad conversion ---
test_value = "abc"
try:
    number = int(test_value)
except ValueError:
    print(f"'{test_value}' is not a valid number.")
# Output:
# 'abc' is not a valid number.


# --- Exercise 20: Multiple except blocks (mini calculator) ---
def divide(a_str, b_str):
    try:
        a = int(a_str)
        b = int(b_str)
        result = a / b
    except ValueError:
        print(f"'{a_str}' or '{b_str}' is not a valid integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"{a} / {b} = {result}")

divide("10", "2")
divide("10", "0")
divide("ten", "2")
# Output:
# 10 / 2 = 5.0
# Cannot divide by zero.
# 'ten' or '2' is not a valid integer.


# --- Exercise 21: Use else ---
try:
    with open("notes.txt") as f:
        text = f.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File loaded successfully")
    print("Length:", len(text))
# Output:
# File loaded successfully
# Length: 135


# --- Exercise 22: Use finally for cleanup logging ---
def try_read(path):
    try:
        with open(path) as f:
            f.read()
        print(f"'{path}' read successfully.")
    except FileNotFoundError:
        print(f"'{path}' was not found.")
    finally:
        print("Attempt finished")

try_read("notes.txt")
try_read("ghost.txt")
# Output:
# 'notes.txt' read successfully.
# Attempt finished
# 'ghost.txt' was not found.
# Attempt finished


# ===================================================================
# PART F: Raising & Creating Custom Exceptions
# ===================================================================

# --- Exercise 23: Raise a built-in exception ---
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

try:
    print("Valid age:", check_age(25))
    print("Invalid age:", check_age(-3))
except ValueError as e:
    print("Error:", e)
# Output:
# Valid age: 25
# Error: Age cannot be negative.


# --- Exercise 24: Define a custom exception ---
class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(f"{score} is not between 0 and 100.")
    return score

try:
    print("Validated:", validate_score(105))
except InvalidScoreError as e:
    print("Error:", e)
# Output:
# Error: 105 is not between 0 and 100.


# --- Exercise 25: Catch your custom exception ---
test_scores = [88, -5, 76, 150, 42]
for s in test_scores:
    try:
        validate_score(s)
        print(f"{s} is valid.")
    except InvalidScoreError as e:
        print(f"{s} is invalid: {e}")
# Output:
# 88 is valid.
# -5 is invalid: -5 is not between 0 and 100.
# 76 is valid.
# 150 is invalid: 150 is not between 0 and 100.
# 42 is valid.


# ===================================================================
# PART G: Cumulative — Files, Exceptions, Functions & Data Structures
# ===================================================================

# --- Exercise 26: Safe score loader (function) ---
def load_scores(path):
    result = {}
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    result[row["name"]] = int(row["score"])
                except ValueError:
                    continue
    except FileNotFoundError:
        return {}
    return result

scores_dict = load_scores("scores.csv")
print("Loaded scores:", scores_dict)
print("Missing file returns:", load_scores("no_such_file.csv"))
# Output:
# Loaded scores: {'Asha': 88, 'Ravi': 105, 'Karan': -5, 'Divya': 76}
# Missing file returns: {}


# --- Exercise 27: Validate and summarise ---
def summarise(scores):
    values = list(scores.values())
    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values),
    }

print(summarise(scores_dict))
# Output:
# {'count': 4, 'average': 66.0, 'highest': 105, 'lowest': -5}


# --- Exercise 28: Word frequency counter ---
def word_frequencies(path):
    freq = {}
    with open(path) as f:
        for line in f:
            for word in line.lower().split():
                freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequencies("notes.txt"))
# Output:
# {'python': 1, 'is': 1, 'fun': 1, 'to': 1, 'learn.': 1, 'files': 1,
#  'can': 1, 'be': 1, 'read': 1, 'line': 1, 'by': 1, 'line.': 1,
#  'csv': 1, 'and': 1, 'json': 1, 'are': 1, 'common': 1, 'data': 1,
#  'formats.': 1, 'exceptions': 1, 'keep': 1, 'programs': 1,
#  'from': 1, 'crashing.': 1}


# --- Exercise 29: JSON config with validation ---
class MissingConfigKeyError(Exception):
    pass

def load_config(path):
    with open(path) as f:
        data = json.load(f)
    if "batch_size" not in data:
        raise MissingConfigKeyError("Missing 'batch_size' in config.")
    if "learning_rate" not in data:
        raise MissingConfigKeyError("Missing 'learning_rate' in config.")
    return data

with open("config_good.json", "w") as f:
    json.dump({"batch_size": 32, "learning_rate": 0.001}, f)

with open("config_bad.json", "w") as f:
    json.dump({"batch_size": 32}, f)   # learning_rate deliberately missing

try:
    print("Good config:", load_config("config_good.json"))
    print("Bad config:", load_config("config_bad.json"))
except MissingConfigKeyError as e:
    print("Config error:", e)
# Output:
# Good config: {'batch_size': 32, 'learning_rate': 0.001}
# Config error: Missing 'learning_rate' in config.


# ===================================================================
# PART H: Assignment 3 Preview — Mini log parser
# ===================================================================

# Setup: access.log with one malformed line (ERROR with no message)
log_lines = [
    "2026-03-23 10:02 ERROR Connection timeout",
    "2026-03-23 10:03 INFO Server started",
    "2026-03-23 10:05 WARNING Disk space low",
    "2026-03-23 10:07 ERROR",              # malformed: missing message
    "2026-03-23 10:09 INFO User login successful",
    "2026-03-23 10:11 DEBUG Cache refreshed",
    "2026-03-23 10:13 ERROR Database connection failed",
]
with open("access.log", "w") as f:
    for line in log_lines:
        f.write(line + "\n")


# --- Exercise 30: Draft a mini log parser ---
def parse_log(path):
    parsed = []
    skipped = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # maxsplit=3 -> exactly 4 tokens: date, time, level, message
            parts = line.split(maxsplit=3)
            if len(parts) < 4:
                skipped += 1
                continue
            timestamp = parts[0] + " " + parts[1]
            level = parts[2]
            message = parts[3]
            parsed.append({
                "timestamp": timestamp,
                "level": level,
                "message": message,
            })
    print(f"Parsed successfully: {len(parsed)}")
    print(f"Skipped (malformed): {skipped}")
    return parsed

log_entries = parse_log("access.log")
for entry in log_entries:
    print(entry)
# Output:
# Parsed successfully: 6
# Skipped (malformed): 1
# {'timestamp': '2026-03-23 10:02', 'level': 'ERROR', 'message': 'Connection timeout'}
# {'timestamp': '2026-03-23 10:03', 'level': 'INFO', 'message': 'Server started'}
# {'timestamp': '2026-03-23 10:05', 'level': 'WARNING', 'message': 'Disk space low'}
# {'timestamp': '2026-03-23 10:09', 'level': 'INFO', 'message': 'User login successful'}
# {'timestamp': '2026-03-23 10:11', 'level': 'DEBUG', 'message': 'Cache refreshed'}
# {'timestamp': '2026-03-23 10:13', 'level': 'ERROR', 'message': 'Database connection failed'}