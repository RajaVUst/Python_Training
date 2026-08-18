import csv
 
with open(r"Day_6\Ref doc\scores.csv", "r") as f:
    reader = csv.reader(f)
 
    header = next(reader)  # Read the header row
    print("Header:", header)
 
    for row in reader:
        print(row)
 
# Output:
"""
Header: ['Name', 'Score']
['Alice', '85']
['Bob', '92']
['Charlie', '78']
"""
 