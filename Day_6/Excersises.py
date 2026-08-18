import csv
import json



with open("notes.txt", "w") as f:
    f.write("Python file handling\n")
    f.write("I learned about CSV files\n")
    f.write("JSON is useful for structured data\n")
    f.write("Exceptions help handle errors\n")
    f.write("Functions make code reusable\n")


# ------------------------------------------------------------
# Exercise 1: Read the whole file
# ------------------------------------------------------------

with open("notes.txt", "r") as f:
    content = f.read()

print("\nExercise 1")
print("Number of characters:", len(content))

# SAMPLE OUTPUT:
# Exercise 1
# Number of characters: 153


# ------------------------------------------------------------
# Exercise 2: Read just the first line
# ------------------------------------------------------------

with open("notes.txt", "r") as f:
    first_line = f.readline().strip()

print("\nExercise 2")
print(first_line)

# SAMPLE OUTPUT:
# Exercise 2
# Python file handling


# ------------------------------------------------------------
# Exercise 3: Read all lines into a list
# ------------------------------------------------------------

with open("notes.txt", "r") as f:
    lines = f.readlines()

print("\nExercise 3")
print("Number of lines:", len(lines))
print(lines)

# SAMPLE OUTPUT:
# Exercise 3
# Number of lines: 5
# ['Python file handling\n', 'I learned about CSV files\n',
#  'JSON is useful for structured data\n',
#  'Exceptions help handle errors\n',
#  'Functions make code reusable\n']


# ------------------------------------------------------------
# Exercise 4: Line-by-line iteration
# ------------------------------------------------------------

print("\nExercise 4")

with open("notes.txt", "r") as f:
    for line in f:
        clean_line = line.strip()

        if not clean_line:
            continue

        print(clean_line.upper())

# SAMPLE OUTPUT:
# Exercise 4
# PYTHON FILE HANDLING
# I LEARNED ABOUT CSV FILES
# JSON IS USEFUL FOR STRUCTURED DATA
# EXCEPTIONS HELP HANDLE ERRORS
# FUNCTIONS MAKE CODE REUSABLE


# ------------------------------------------------------------
# Exercise 5: Count words in a file
# ------------------------------------------------------------

word_count = 0

with open("notes.txt", "r") as f:
    for line in f:
        word_count += len(line.split())

print("\nExercise 5")
print("Total number of words:", word_count)

# SAMPLE OUTPUT:
# Exercise 5
# Total number of words: 23


# ============================================================
# PART B: WRITING & APPENDING FILES
# ============================================================

# ------------------------------------------------------------
# Exercise 6: Write a fresh file
# ------------------------------------------------------------

with open("diary.txt", "w") as f:
    f.write("I learned how to read files.\n")
    f.write("I learned how to work with CSV and JSON.\n")
    f.write("I learned how to handle exceptions.\n")

print("\nExercise 6")
print("diary.txt created successfully.")

# SAMPLE OUTPUT:
# Exercise 6
# diary.txt created successfully.


# ------------------------------------------------------------
# Exercise 7: Append without overwriting
# ------------------------------------------------------------

with open("diary.txt", "a") as f:
    f.write("I practiced raising custom exceptions.\n")

with open("diary.txt", "r") as f:
    diary_content = f.read()

print("\nExercise 7")
print(diary_content)

# SAMPLE OUTPUT:
# Exercise 7
# I learned how to read files.
# I learned how to work with CSV and JSON.
# I learned how to handle exceptions.
# I practiced raising custom exceptions.


# ------------------------------------------------------------
# Exercise 8: Write numbers to a file
# ------------------------------------------------------------

with open("squares.txt", "w") as f:
    for number in range(1, 11):
        square = number ** 2
        f.write(str(square) + "\n")

total = 0

with open("squares.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("\nExercise 8")
print("Total of squares:", total)

# SAMPLE OUTPUT:
# Exercise 8
# Total of squares: 385


# ------------------------------------------------------------
# Exercise 9: Copy and transform a file
# ------------------------------------------------------------

with open("notes.txt", "r") as source:
    with open("notes_upper.txt", "w") as destination:
        for line in source:
            destination.write(line.upper())

print("\nExercise 9")
print("Uppercase copy created successfully.")

# SAMPLE OUTPUT:
# Exercise 9
# Uppercase copy created successfully.


# ============================================================
# PART C: WORKING WITH CSV FILES
# ============================================================

# Create scores.csv
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "score"])
    writer.writerow(["Asha", "85"])
    writer.writerow(["Rahul", "105"])
    writer.writerow(["Meena", "92"])
    writer.writerow(["Vikram", ""])
    writer.writerow(["Priya", "-10"])


# ------------------------------------------------------------
# Exercise 10: Read CSV with csv.reader
# ------------------------------------------------------------

print("\nExercise 10")

with open("scores.csv", "r", newline="") as f:
    reader = csv.reader(f)

    header = next(reader)

    print("Header:", header)

    for row in reader:
        print(row)

# SAMPLE OUTPUT:
# Exercise 10
# Header: ['name', 'score']
# ['Asha', '85']
# ['Rahul', '105']
# ['Meena', '92']
# ['Vikram', '']
# ['Priya', '-10']


# ------------------------------------------------------------
# Exercise 11: Read CSV with DictReader
# ------------------------------------------------------------

print("\nExercise 11")

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['score']}")

# SAMPLE OUTPUT:
# Exercise 11
# Asha: 85
# Rahul: 105
# Meena: 92
# Vikram:
# Priya: -10


# ------------------------------------------------------------
# Exercise 12: Compute average from CSV data
# ------------------------------------------------------------

scores = []

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))
        else:
            continue

average = sum(scores) / len(scores)

print("\nExercise 12")
print("Average:", average)

# SAMPLE OUTPUT:
# Exercise 12
# Average: 68.0


# ------------------------------------------------------------
# Exercise 13: Write a CSV file
# ------------------------------------------------------------

students = [
    ["Asha", 88],
    ["Rahul", 91],
    ["Meena", 79],
    ["Priya", 95]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "score"])
    writer.writerows(students)

print("\nExercise 13")
print("results.csv created successfully.")

# SAMPLE OUTPUT:
# Exercise 13
# results.csv created successfully.


# ============================================================
# PART D: WORKING WITH JSON FILES
# ============================================================

# Create profile.json
profile = {
    "name": "Asha",
    "track": "Python Readiness",
    "completed_days": [1, 2, 3, 4, 5]
}

with open("profile.json", "w") as f:
    json.dump(profile, f, indent=2)


# ------------------------------------------------------------
# Exercise 14: Read a JSON file
# ------------------------------------------------------------

with open("profile.json", "r") as f:
    profile_data = json.load(f)

print("\nExercise 14")
print("Name:", profile_data["name"])
print("Completed days:", len(profile_data["completed_days"]))

# SAMPLE OUTPUT:
# Exercise 14
# Name: Asha
# Completed days: 5


# ------------------------------------------------------------
# Exercise 15: Modify and re-save JSON
# ------------------------------------------------------------

with open("profile.json", "r") as f:
    profile_data = json.load(f)

profile_data["completed_days"].append(6)

with open("profile.json", "w") as f:
    json.dump(profile_data, f, indent=2)

print("\nExercise 15")
print("Day 6 added to profile.")

# SAMPLE OUTPUT:
# Exercise 15
# Day 6 added to profile.


# ------------------------------------------------------------
# Exercise 16: String <-> JSON with loads/dumps
# ------------------------------------------------------------

session = {
    "topic": "File Handling and Exceptions",
    "duration_minutes": 120,
    "format": "Hands-on Lab"
}

json_string = json.dumps(session)

print("\nExercise 16")
print("JSON string:")
print(json_string)

session_again = json.loads(json_string)

print("Type after loads():", type(session_again))

# SAMPLE OUTPUT:
# Exercise 16
# JSON string:
# {"topic": "File Handling and Exceptions", "duration_minutes": 120, "format": "Hands-on Lab"}
# Type after loads(): <class 'dict'>


# ------------------------------------------------------------
# Exercise 17: CSV to JSON
# ------------------------------------------------------------

rows = []

with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        rows.append(dict(row))

with open("scores.json", "w") as f:
    json.dump(rows, f, indent=2)

print("\nExercise 17")
print("scores.json created successfully.")

# SAMPLE OUTPUT:
# Exercise 17
# scores.json created successfully.


# ============================================================
# PART E: TRY / EXCEPT / ELSE / FINALLY
# ============================================================

# ------------------------------------------------------------
# Exercise 18: Catch a missing file
# ------------------------------------------------------------

print("\nExercise 18")

try:
    with open("ghost.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("Sorry, the file was not found.")

# SAMPLE OUTPUT:
# Exercise 18
# Sorry, the file was not found.


# ------------------------------------------------------------
# Exercise 19: Catch a bad conversion
# ------------------------------------------------------------

print("\nExercise 19")

value = "abc"

try:
    number = int(value)
    print("Converted number:", number)

except ValueError:
    print("Invalid input. Please enter a valid integer.")

# SAMPLE OUTPUT:
# Exercise 19
# Invalid input. Please enter a valid integer.


# ------------------------------------------------------------
# Exercise 20: Multiple except blocks
# ------------------------------------------------------------

print("\nExercise 20")

first_input = "20"
second_input = "0"

try:
    first_number = int(first_input)
    second_number = int(second_input)

    result = first_number / second_number

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# SAMPLE OUTPUT:
# Exercise 20
# Cannot divide by zero.


# ------------------------------------------------------------
# Exercise 21: Use else
# ------------------------------------------------------------

print("\nExercise 21")

try:
    with open("notes.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    print("The file could not be found.")

else:
    print("File loaded successfully.")
    print("File length:", len(content))

# SAMPLE OUTPUT:
# Exercise 21
# File loaded successfully.
# File length: 153


# ------------------------------------------------------------
# Exercise 22: Use finally
# ------------------------------------------------------------

print("\nExercise 22")

# Test with an existing file
try:
    with open("notes.txt", "r") as f:
        content = f.read()

    print("Existing file read successfully.")

except FileNotFoundError:
    print("File does not exist.")

finally:
    print("Attempt finished")


# Test with a missing file
try:
    with open("missing_file.txt", "r") as f:
        content = f.read()

    print("Missing file read successfully.")

except FileNotFoundError:
    print("File does not exist.")

finally:
    print("Attempt finished")

# SAMPLE OUTPUT:
# Exercise 22
# Existing file read successfully.
# Attempt finished
# File does not exist.
# Attempt finished


# ============================================================
# PART F: RAISING & CREATING CUSTOM EXCEPTIONS
# ============================================================

# ------------------------------------------------------------
# Exercise 23: Raise a built-in exception
# ------------------------------------------------------------

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


print("\nExercise 23")

try:
    print("Valid age:", check_age(25))

except ValueError as e:
    print("Error:", e)


try:
    print("Invalid age:", check_age(-5))

except ValueError as e:
    print("Error:", e)

# SAMPLE OUTPUT:
# Exercise 23
# Valid age: 25
# Error: Age cannot be negative.


# ------------------------------------------------------------
# Exercise 24: Define a custom exception
# ------------------------------------------------------------

class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")

    return score


print("\nExercise 24")

print("Valid score:", validate_score(85))

# SAMPLE OUTPUT:
# Exercise 24
# Valid score: 85


# ------------------------------------------------------------
# Exercise 25: Catch your custom exception
# ------------------------------------------------------------

test_scores = [85, 105, 70, -10, 95]

print("\nExercise 25")

for score in test_scores:

    try:
        valid_score = validate_score(score)
        print(f"{score} is valid.")

    except InvalidScoreError as e:
        print(f"{score} is invalid: {e}")

# SAMPLE OUTPUT:
# Exercise 25
# 85 is valid.
# 105 is invalid: Score must be between 0 and 100.
# 70 is valid.
# -10 is invalid: Score must be between 0 and 100.
# 95 is valid.


# ============================================================
# PART G: CUMULATIVE
# ============================================================

# ------------------------------------------------------------
# Exercise 26: Safe score loader
# ------------------------------------------------------------

def load_scores(path):

    scores = {}

    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:

                try:
                    score = int(row["score"])

                except (ValueError, TypeError):
                    continue

                scores[row["name"]] = score

    except FileNotFoundError:
        return {}

    return scores


print("\nExercise 26")

loaded_scores = load_scores("scores.csv")

print("Loaded scores:")
print(loaded_scores)

# SAMPLE OUTPUT:
# Exercise 26
# Loaded scores:
# {'Asha': 85, 'Rahul': 105, 'Meena': 92, 'Priya': -10}


# ------------------------------------------------------------
# Exercise 27: Validate and summarise
# ------------------------------------------------------------

def summarise(scores):

    if not scores:
        return {
            "count": 0,
            "average": 0,
            "highest": None,
            "lowest": None
        }

    values = scores.values()

    return {
        "count": len(scores),
        "average": sum(values) / len(scores),
        "highest": max(values),
        "lowest": min(values)
    }


print("\nExercise 27")

summary = summarise(loaded_scores)

print(summary)

# SAMPLE OUTPUT:
# Exercise 27
# {'count': 4, 'average': 68.0, 'highest': 105, 'lowest': -10}


# ------------------------------------------------------------
# Exercise 28: Word frequency counter
# ------------------------------------------------------------

def word_frequencies(path):

    frequencies = {}

    try:
        with open(path, "r") as f:

            for line in f:

                words = line.lower().split()

                for word in words:

                    # Optional punctuation removal
                    word = word.strip(".,!?;:'\"()[]{}")

                    if not word:
                        continue

                    frequencies[word] = frequencies.get(word, 0) + 1

    except FileNotFoundError:
        return {}

    return frequencies


print("\nExercise 28")

frequencies = word_frequencies("notes.txt")

print(frequencies)

# SAMPLE OUTPUT:
# Exercise 28
# {
# 'python': 1,
# 'file': 2,
# 'handling': 1,
# 'i': 1,
# 'learned': 2,
# 'about': 2,
# 'csv': 1,
# 'files': 1,
# 'json': 1,
# 'is': 1,
# 'useful': 1,
# 'for': 2,
# 'structured': 1,
# 'data': 1,
# 'exceptions': 1,
# 'help': 1,
# 'errors': 1,
# 'functions': 1,
# 'make': 1,
# 'code': 1,
# 'reusable': 1
# }


# ------------------------------------------------------------
# Exercise 29: JSON config with validation
# ------------------------------------------------------------

class MissingConfigKeyError(Exception):
    pass


def load_config(path):

    with open(path, "r") as f:
        data = json.load(f)

    if "batch_size" not in data:
        raise MissingConfigKeyError(
            "Missing required configuration key: batch_size"
        )

    if "learning_rate" not in data:
        raise MissingConfigKeyError(
            "Missing required configuration key: learning_rate"
        )

    return data


# Create a sample config file
with open("config.json", "w") as f:
    json.dump({
        "batch_size": 32,
        "learning_rate": 0.001
    }, f, indent=2)


print("\nExercise 29")

try:
    config = load_config("config.json")
    print("Config loaded successfully:")
    print(config)

except MissingConfigKeyError as e:
    print("Configuration error:", e)

except FileNotFoundError:
    print("Configuration file not found.")

# SAMPLE OUTPUT:
# Exercise 29
# Config loaded successfully:
# {'batch_size': 32, 'learning_rate': 0.001}


# ============================================================
# PART H: ASSIGNMENT 3 PREVIEW
# ============================================================

# ------------------------------------------------------------
# Exercise 30: Draft a mini log parser
# ------------------------------------------------------------

# Create sample access.log
with open("access.log", "w") as f:
    f.write("2026-03-23 10:02 ERROR Connection timeout\n")
    f.write("2026-03-23 10:05 INFO User logged in\n")
    f.write("2026-03-23 10:10 WARNING Disk space low\n")
    f.write("2026-03-23 ERROR Missing timestamp\n")
    f.write("2026-03-23 10:15 INFO File uploaded successfully\n")
    f.write("MALFORMED LINE\n")
    f.write("2026-03-23 10:20 ERROR Database connection failed\n")
    f.write("2026-03-23 10:25 INFO Process completed\n")


def parse_log(path):

    parsed_logs = []
    skipped_lines = 0

    try:
        with open(path, "r") as f:

            for line in f:

                clean_line = line.strip()

                if not clean_line:
                    continue

                parts = clean_line.split(maxsplit=3)

                # Expected structure:
                # date time LEVEL message
                #
                # Example:
                # 2026-03-23 10:02 ERROR Connection timeout
                #
                # parts[0] = date
                # parts[1] = time
                # parts[2] = level
                # parts[3] = message

                if len(parts) < 4:
                    skipped_lines += 1
                    continue

                date = parts[0]
                time = parts[1]
                level = parts[2]
                message = parts[3]

                # Basic validation
                if len(date) != 10 or date[4] != "-" or date[7] != "-":
                    skipped_lines += 1
                    continue

                if len(time) != 5 or time[2] != ":":
                    skipped_lines += 1
                    continue

                if level not in ["ERROR", "INFO", "WARNING"]:
                    skipped_lines += 1
                    continue

                timestamp = date + " " + time

                parsed_logs.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message
                })

    except FileNotFoundError:
        print("Log file not found.")
        return [], 0

    return parsed_logs, skipped_lines


print("\nExercise 30")

logs, skipped = parse_log("access.log")

print("Successfully parsed:", len(logs))
print("Skipped:", skipped)

print("\nParsed log entries:")

for log in logs:
    print(log)

# SAMPLE OUTPUT:
# Exercise 30
# Successfully parsed: 6
# Skipped: 2
#
# Parsed log entries:
# {'timestamp': '2026-03-23 10:02',
#  'level': 'ERROR',
#  'message': 'Connection timeout'}
#
# {'timestamp': '2026-03-23 10:05',
#  'level': 'INFO',
#  'message': 'User logged in'}
#
# {'timestamp': '2026-03-23 10:10',
#  'level': 'WARNING',
#  'message': 'Disk space low'}
#
# {'timestamp': '2026-03-23 10:15',
#  'level': 'INFO',
#  'message': 'File uploaded successfully'}
#
# {'timestamp': '2026-03-23 10:20',
#  'level': 'ERROR',
#  'message': 'Database connection failed'}
#
# {'timestamp': '2026-03-23 10:25',
#  'level': 'INFO',
#  'message': 'Process completed'}



print("\n" + "=" * 60)
print("DAY 6 PRACTICE LAB COMPLETE")
print("=" * 60)

