# Exercise 14: Read a JSON file
import json, csv
with open("profile.json","r") as f:
    record = json.load(f)
    print(record['name'],record['completed_days'])  # Shabanam [1,2,3,4,5]

# Exercise 15: Modify and re-save JSON
with open("profile.json","r") as f:
    data = json.load(f)
    data['completed_days'].append(6)

with open("profile.json","w") as f:
    json.dump(data,f,indent = 2)
""" Output file ->
{
  "name": "Shabanam",
  "track": "HR",
  "completed_days": [1, 2, 3, 4, 5, 6]
}   """

# Exercise 16: String <-> JSON with loads/dumps
session = {"topic":"Files", "duration_minutes": 120, "format": "JSON"}
json_str = json.dumps(session)
print(json_str)     # {"topic": "Files", "duration_minutes": 120, "format": "JSON"}
back_to_dict = json.loads(json_str)
print(type(back_to_dict))   # <class 'dict'>

# Exercise 17: CSV to JSON
li = []
with open("scores.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        li.append(dict(row))
with open("scores.json","w") as f:
    json.dump(li,f,indent = 2)
"""
Output file ->
[
  {
    "Name": "Shabanam",
    "Score": "100"
  },
  {
    "Name": "Arsha",
    "Score": "96"
  },
  {
    "Name": "Reni",
    "Score": "179"
  },
  {
    "Name": "Raja",
    "Score": "86"
  },
  {
    "Name": "Anjitha",
    "Score": ""
  }
] """