# Exercise 10: Read a CSV with csv.reader
import csv

with open("scores.csv","r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)       # ['Name', 'Score']
    for row in reader:
        print(row)
""" Output ->
['Shabanam', '100']
['Arsha', '96']
['Reni', '179']
['Raja', '86']
['Anjitha', ''] """

# Exercise 11: Read a CSV with DictReader
with open("scores.csv","r", newline = "") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"<{row['Name']}>: <{row['Score']}>")
""" Output ->
<Shabanam>: <100>
<Arsha>: <96>
<Reni>: <179>
<Raja>: <86>
<Anjitha>: <> """

# Exercise 12: Compute an average from CSV data
with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)
    l = []
    for row in reader:
        if row["Score"] != "":
            l.append(int(row['Score']))
    print(sum(l)/len(l))    # 115.25

# Exercise 13: Write a CSV file
scores = [["Bharath",95],["Didina",87],["Bhaskar",90],["Uday",99]]
with open("results.csv","w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(['name','score'])
    writer.writerows(scores)

""" 
Oytput file -->
name,score
Bharath,95
Didina,87
Bhaskar,90
Uday,99 """