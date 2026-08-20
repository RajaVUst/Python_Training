# Exercise 10: Read a CSV with csv.reader 

import csv
with open('scores.csv', "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(row)
# Output
# ['senin', '65']
# ['akshay', '80']
# ['ameen', '86']
# ['ashik', '77']
# ['gokul', '']

# 11: Read a CSV with DictReader
import csv 
with open('scores.csv', "r") as f:
    reader = csv.DictReader(f)
    header = next(reader)
    for row in reader:
        print(row)

# Output 

# {'Name ': 'akshay', 'score': '80'}
# {'Name ': 'ameen', 'score': '86'}
# {'Name ': 'ashik', 'score': '77'}
# {'Name ': 'gokul', 'score': ''}

# Exercise 12: Compute an average from CSV data 

import csv 
scores = []
with open('scores.csv', "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['score'].isdigit():
            scores.append(int(row["score"]))
        else:
            print('Invalid')
avg = sum(scores)/len(scores)
print('average :', avg)

# output

# Invalid
# Invalid
# average : 77.0

# Exercise 13: Write a CSV file 

import csv 

rows = [["name", "score"], ["sana", "100"], ["suresh", "60"], ["sid", "80"], ["akash", "86"]]
with open('results.csv', "w", newline="")as f:
    writer = csv.writer(f)
    writer.writerows(rows)