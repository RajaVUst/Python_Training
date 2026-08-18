import json
import csv

# Exercise 14
print("Exercise 14")

with open("profile.json", "r") as f:
    profile = json.load(f)

print("Name:", profile["name"])
print("Completed Days:", len(profile["completed_days"]))

print()

# Exercise 15
print("Exercise 15")

profile["completed_days"].append(6)

with open("profile.json", "w") as f:
    json.dump(profile, f, indent=2)

print("profile.json updated.")

print()

# Exercise 16
print("Exercise 16")

session = {
    "topic": "Lists, Tuples, Sets, Dictionaries",
    "duration_minutes": 120,
    "format": "Classroom"
}

json_string = json.dumps(session)

print(json_string)

data = json.loads(json_string)

print("Type:", type(data))

print()

# Exercise 17
print("Exercise 17")

records = []

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        records.append(dict(row))

with open("scores.json", "w") as f:
    json.dump(records, f, indent=2)

print("scores.json created successfully.")

#output
'''Exercise 14
Name: JS
Completed Days: 5

Exercise 15
profile.json updated.

Exercise 16
{"topic": "Lists, Tuples, Sets, Dictionaries", "duration_minutes": 120, "format": "Classroom"}
Type: <class 'dict'>

Exercise 17
scores.json created successfully.
'''