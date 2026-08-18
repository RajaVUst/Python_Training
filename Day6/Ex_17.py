import csv
import json
 
rows = []
 
with open(r"Day_6\Ref doc\scores.csv", "r") as f:
    reader = csv.DictReader(f)
 
    for row in reader:
        rows.append(dict(row))
 
with open(r"Day_6\Ref doc\scores.json", "w") as f:
    json.dump(rows, f, indent=2)
 
print("scores.json created successfully!")
 
# Output:
# scores.json created successfully!
 