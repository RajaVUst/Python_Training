
import csv
import json


# Part A: Reading Files


with open("notes.txt", "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("Files store information.\n")
    f.write("Lists can hold many values.\n")
    f.write("Dictionaries store key-value pairs.\n")
    f.write("Functions help organize code.\n")


# Exercise 1: Read the whole file

with open("notes.txt", "r") as f:
    content = f.read()

print("Exercise 1:")

# Output: Number of characters: 139
print("Number of characters:", len(content))


# Exercise 2: Read just the first line

with open("notes.txt", "r") as f:
    first_line = f.readline()

print("\nExercise 2:")

# Output: Python is easy to learn.
print(first_line.strip())


# Exercise 3: Read all lines into a list

with open("notes.txt", "r") as f:
    lines = f.readlines()

print("\nExercise 3:")

# Output: Number of lines: 5
print("Number of lines:", len(lines))

# Output:
# ['Python is easy to learn.\n',
#  'Files store information.\n',
#  'Lists can hold many values.\n',
#  'Dictionaries store key-value pairs.\n',
#  'Functions help organize code.\n']
print(lines)


# Exercise 4: Line-by-line iteration

print("\nExercise 4:")

with open("notes.txt", "r") as f:

    for line in f:

        clean_line = line.strip()

        if not clean_line:
            continue

        # Output:
        # PYTHON IS EASY TO LEARN.
        # FILES STORE INFORMATION.
        # LISTS CAN HOLD MANY VALUES.
        # DICTIONARIES STORE KEY-VALUE PAIRS.
        # FUNCTIONS HELP ORGANIZE CODE.
        print(clean_line.upper())


# Exercise 5: Count words in a file

word_count = 0

with open("notes.txt", "r") as f:

    for line in f:

        words = line.split()
        word_count = word_count + len(words)

print("\nExercise 5:")

# Output: Total number of words: 25
print("Total number of words:", word_count)


# Part B: Writing & Appending Files

# Exercise 6: Write a fresh file

with open("diary.txt", "w") as f:

    f.write("I learned how to read files.\n")
    f.write("I learned how to write files.\n")
    f.write("I learned how to use dictionaries.\n")

print("\nExercise 6:")

# Output: diary.txt created.
print("diary.txt created.")


# Exercise 7: Append without overwriting

with open("diary.txt", "a") as f:

    f.write("I learned how to handle exceptions.\n")


with open("diary.txt", "r") as f:

    diary = f.read()

print("\nExercise 7:")

# Output:
# I learned how to read files.
# I learned how to write files.
# I learned how to use dictionaries.
# I learned how to handle exceptions.
print(diary)


# Exercise 8: Write numbers to a file

with open("squares.txt", "w") as f:

    for number in range(1, 11):

        square = number * number

        f.write(str(square) + "\n")


total = 0

with open("squares.txt", "r") as f:

    for line in f:

        total = total + int(line.strip())

print("Exercise 8:")

# Output: Total of squares: 385
print("Total of squares:", total)


# Exercise 9: Copy and transform a file

with open("notes.txt", "r") as source:

    with open("notes_upper.txt", "w") as destination:

        for line in source:

            destination.write(line.upper())


print("\nExercise 9:")

# Output: notes_upper.txt created.
print("notes_upper.txt created.")


# Part C: Working with CSV Files

# Create scores.csv

with open("scores.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(["name", "score"])
    writer.writerow(["Amit", "78"])
    writer.writerow(["Reni", "91"])
    writer.writerow(["Tara", "105"])
    writer.writerow(["John", ""])
    writer.writerow(["David", "65"])


# Exercise 10: Read a CSV with csv.reader

print("\nExercise 10:")

with open("scores.csv", "r", newline="") as f:

    reader = csv.reader(f)

    header = next(reader)

    # Output: Header: ['name', 'score']
    print("Header:", header)

    for row in reader:

        # Output:
        # ['Amit', '78']
        # ['Reni', '91']
        # ['Tara', '105']
        # ['John', '']
        # ['David', '65']
        print(row)


# Exercise 11: Read a CSV with DictReader

print("\nExercise 11:")

with open("scores.csv", "r", newline="") as f:

    reader = csv.DictReader(f)

    for row in reader:

        # Output:
        # Amit: 78
        # Reni: 91
        # Tara: 105
        # John:
        # David: 65
        print(row["name"] + ": " + row["score"])


# Exercise 12: Compute an average from CSV data

scores = []

with open("scores.csv", "r", newline="") as f:

    reader = csv.DictReader(f)

    for row in reader:

        if row["score"] != "":

            scores.append(int(row["score"]))

        else:

            # Output: Skipping blank score for: John
            print("Skipping blank score for:", row["name"])


average = sum(scores) / len(scores)

print("\nExercise 12:")

# Output: Average: 84.75
print("Average:", average)


# Exercise 13: Write a CSV file

students = [
    ["Amit", 78],
    ["Reni", 91],
    ["Tara", 85],
    ["John", 72]
]

with open("results.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(["name", "score"])

    for student in students:

        writer.writerow(student)


print("\nExercise 13:")

# Output: results.csv created.
print("results.csv created.")


# Part D: Working with JSON Files


profile = {
    "name": "Asha",
    "track": "Python Readiness",
    "completed_days": [1, 2, 3, 4, 5]
}

with open("profile.json", "w") as f:

    json.dump(profile, f, indent=2)


# Exercise 14: Read a JSON file

with open("profile.json", "r") as f:

    profile = json.load(f)


print("\nExercise 14:")

# Output: Name: Asha
print("Name:", profile["name"])

# Output: Completed days: 5
print("Completed days:", len(profile["completed_days"]))


# Exercise 15: Modify and re-save JSON

with open("profile.json", "r") as f:

    profile = json.load(f)


profile["completed_days"].append(6)


with open("profile.json", "w") as f:

    json.dump(profile, f, indent=2)


print("\nExercise 15:")

# Output: Added day 6 to completed_days.
print("Added day 6 to completed_days.")


# Exercise 16: String <-> JSON with loads/dumps

session = {
    "topic": "File Handling",
    "duration_minutes": 60,
    "format": "Practice"
}

json_string = json.dumps(session)

print("\nExercise 16:")

# Output:
# {"topic": "File Handling", "duration_minutes": 60, "format": "Practice"}
print(json_string)


session_again = json.loads(json_string)

# Output: <class 'dict'>
print(type(session_again))


# Exercise 17: CSV to JSON

rows = []

with open("scores.csv", "r", newline="") as f:

    reader = csv.DictReader(f)

    for row in reader:

        rows.append(dict(row))


with open("scores.json", "w") as f:

    json.dump(rows, f, indent=2)


print("\nExercise 17:")

# Output: scores.json created.
print("scores.json created.")


# Part E: try / except / else / finally

# Exercise 18: Catch a missing file

print("\nExercise 18:")

try:

    with open("ghost.txt", "r") as f:

        content = f.read()

except FileNotFoundError:

    # Output: The file ghost.txt was not found.
    print("The file ghost.txt was not found.")


# Exercise 19: Catch a bad conversion

print("\nExercise 19:")

value = "abc"

try:

    number = int(value)

    # This won't execute
    print("Number:", number)

except ValueError:

    # Output: The value cannot be converted to an integer.
    print("The value cannot be converted to an integer.")


# Exercise 20: Multiple except blocks

print("\nExercise 20:")


first = input("Enter the first number: ")
second = input("Enter the second number: ")


try:

    number1 = int(first)
    number2 = int(second)

    result = number1 / number2

    # Example output: Result: 5.0
    print("Result:", result)


except ValueError:

    # Output if invalid input is entered:
    # Please enter valid numbers.
    print("Please enter valid numbers.")


except ZeroDivisionError:

    # Output if second number is 0:
    # You cannot divide by zero.
    print("You cannot divide by zero.")


# Exercise 21: Use else

print("\nExercise 21:")


try:

    with open("notes.txt", "r") as f:

        content = f.read()


except FileNotFoundError:

    print("The file was not found.")


else:

    # Output: File loaded successfully
    print("File loaded successfully")

    # Output: File length: 139
    print("File length:", len(content))


# Exercise 22: Use finally for cleanup logging

print("\nExercise 22:")


try:

    with open("notes.txt", "r") as f:

        content = f.read()

except FileNotFoundError:

    print("The file was not found.")

finally:

    # Output: Attempt finished
    print("Attempt finished")



try:

    with open("missing.txt", "r") as f:

        content = f.read()

except FileNotFoundError:

    # Output: The file was not found.
    print("The file was not found.")

finally:

    # Output: Attempt finished
    print("Attempt finished")


# Part F: Raising & Creating Custom Exceptions
# Exercise 23: Raise a built-in exception

def check_age(age):

    if age < 0:

        raise ValueError("Age cannot be negative.")

    return age


print("\nExercise 23:")


try:

    # Output: Valid age: 25
    print("Valid age:", check_age(25))

except ValueError as error:

    print("Error:", error)


try:

    # This raises an error
    print("Invalid age:", check_age(-5))

except ValueError as error:

    # Output: Error: Age cannot be negative.
    print("Error:", error)


# Exercise 24: Define a custom exception


class InvalidScoreError(Exception):
    pass


def validate_score(score):

    if score < 0 or score > 100:

        raise InvalidScoreError(
            "Score must be between 0 and 100."
        )

    return score


print("\nExercise 24:")


try:

    # Output: Valid score: 85
    print("Valid score:", validate_score(85))

except InvalidScoreError as error:

    print("Error:", error)


# Exercise 25: Catch your custom exception


test_scores = [90, 75, -5, 105, 60]

print("\nExercise 25:")


for score in test_scores:

    try:

        valid_score = validate_score(score)

        # Output:
        # Valid score: 90
        # Valid score: 75
        # Valid score: 60
        print("Valid score:", valid_score)

    except InvalidScoreError as error:

        # Output:
        # Invalid score: -5
        # Error: Score must be between 0 and 100.
        #
        # Invalid score: 105
        # Error: Score must be between 0 and 100.
        print("Invalid score:", score)
        print("Error:", error)


# Part G: Cumulative
# Exercise 26: Safe score loader


def load_scores(path):

    scores = {}

    try:

        with open(path, "r", newline="") as f:

            reader = csv.DictReader(f)

            for row in reader:

                try:

                    score = int(row["score"])

                    scores[row["name"]] = score

                except ValueError:

                    # Output: Skipping bad score for: John
                    print("Skipping bad score for:", row["name"])

    except FileNotFoundError:

        print("File not found:", path)

        return {}

    return scores


print("\nExercise 26:")

loaded_scores = load_scores("scores.csv")

# Output:
# {'Amit': 78, 'Reni': 91, 'Tara': 105, 'David': 65}
print(loaded_scores)


# Exercise 27: Validate and summarise


def summarise(scores):

    result = {
        "count": len(scores),
        "average": sum(scores.values()) / len(scores),
        "highest": max(scores.values()),
        "lowest": min(scores.values())
    }

    return result


print("\nExercise 27:")

# Output:
# {'count': 4, 'average': 84.75, 'highest': 105, 'lowest': 65}
print(summarise(loaded_scores))


# Exercise 28: Word frequency counter


def word_frequencies(path):

    word_counts = {}

    with open(path, "r") as f:

        for line in f:

            words = line.lower().split()

            for word in words:

                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


print("\nExercise 28:")

# Output:
# {'python': 1, 'is': 1, 'easy': 1, 'to': 1, 'learn.': 1,
#  'files': 1, 'store': 1, 'information.': 1, ...}
print(word_frequencies("notes.txt"))


# Exercise 29: JSON config with validation


class MissingConfigKeyError(Exception):
    pass


def load_config(path):

    with open(path, "r") as f:

        data = json.load(f)


    if "batch_size" not in data:

        raise MissingConfigKeyError(
            "batch_size is missing."
        )


    if "learning_rate" not in data:

        raise MissingConfigKeyError(
            "learning_rate is missing."
        )


    return data



with open("config.json", "w") as f:

    json.dump(
        {
            "batch_size": 32,
            "learning_rate": 0.01
        },
        f,
        indent=2
    )


print("\nExercise 29:")


try:

    config = load_config("config.json")

    # Output:
    # {'batch_size': 32, 'learning_rate': 0.01}
    print(config)


except MissingConfigKeyError as error:

    print("Config error:", error)


except FileNotFoundError:

    print("Config file was not found.")


# Part H

# Exercise 30: Draft a mini log parser


with open("access.log", "w") as f:

    f.write(
        "2026-03-23 10:02 ERROR Connection timeout\n"
    )

    f.write(
        "2026-03-23 10:05 INFO User logged in\n"
    )

    f.write(
        "2026-03-23 10:10 WARNING Low disk space\n"
    )

    f.write(
        "2026-03-23 10:15\n"
    )

    f.write(
        "2026-03-23 10:20 INFO File uploaded successfully\n"
    )

    f.write(
        "2026-03-23 10:25 ERROR Database connection failed\n"
    )

    f.write(
        "2026-03-23 10:30 INFO Process completed\n"
    )


def parse_log(path):

    parsed_logs = []
    skipped = 0

    with open(path, "r") as f:

        for line in f:

            line = line.strip()

            if not line:

                continue


            parts = line.split(maxsplit=2)


            if len(parts) != 3:

                skipped = skipped + 1

                continue


            timestamp = parts[0] + " " + parts[1]

            level = parts[2].split()[0]

            message = " ".join(
                parts[2].split()[1:]
            )


            if level not in ["ERROR", "INFO", "WARNING"]:

                skipped = skipped + 1

                continue


            if not message:

                skipped = skipped + 1

                continue


            log_entry = {
                "timestamp": timestamp,
                "level": level,
                "message": message
            }


            parsed_logs.append(log_entry)


    return parsed_logs, skipped


print("\nExercise 30:")


logs, skipped_lines = parse_log("access.log")


# Output: Successfully parsed: 6
print("Successfully parsed:", len(logs))

# Output: Skipped: 1
print("Skipped:", skipped_lines)


for log in logs:

    # Example output:
    # {'timestamp': '2026-03-23 10:02',
    #  'level': 'ERROR',
    #  'message': 'Connection timeout'}
    print(log)
