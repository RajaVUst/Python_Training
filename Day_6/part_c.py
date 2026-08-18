import csv

# Exercise 10

with open("scores.csv", "r") as f:
    reader = csv.reader(f)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

print()


# Exercise 11

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['score']}")

print()


# Exercise 12

scores = []

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["score"] != "":
            scores.append(int(row["score"]))

average = sum(scores) / len(scores)

print(f"Average Score: {average:.2f}")
print()


# Exercise 13

students = [
    ["Amit", 78],
    ["Reni", 91],
    ["Tara", 85],
    ["Sam", 67]
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "score"])

    for student in students:
        writer.writerow(student)

print("results.csv created successfully.")


#output
'''Exercise 10
Header: ['name', 'score']
['Amit', '78']
['Reni', '91']
['Tara', '85']
['Sam', '67']
['Priya', '']

Exercise 11
Amit: 78
Reni: 91
Tara: 85
Sam: 67
Priya: 

Exercise 12
Average Score: 80.25

Exercise 13
results.csv created successfully.
'''