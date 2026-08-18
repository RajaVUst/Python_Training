import csv
 
with open(r"Day_6\Ref doc\scores.csv", "r") as f:
    reader = csv.DictReader(f)
 
    for row in reader:
        print(f"{row['Name']}: {row['Score']}")
 
# Output:
# Alice: 85
# Bob: 92  
# Charlie: 78
 