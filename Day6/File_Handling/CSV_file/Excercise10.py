# Read a CSV with csv.reader

import csv

with open("Day6/scores.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    
    for row in reader:
        print(row)

# Output:
# ['name', 'score']
# ['Gokul', '80']
# ['Bala', '95']
# ['Jeeva', '110']
# ['Timmy', '']
# ['Logesh', '70']