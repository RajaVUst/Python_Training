# Exercise 14: Read a JSON file 

import json
with open('profile.json', "r")as f:
    data = json.load(f)
    print(f'Name: {data['name']}, Completed days: {len(data['completed_days'])}')

# output

# Name: Asha, Completed days: 5

# Exercise 15: Modify and re-save JSON 

import json
with open("profile.json", "r") as f:
    profile = json.load(f)
if 6 not in profile["completed_days"]:
    profile["completed_days"].append(6)
with open("profile.json", "w") as f:
    json.dump(profile, f, indent=2)

# Exercise 16: String <-> JSON with loads/dumps 

import json

session = {
    "topic": "JSOn",
    "duration": 10,
    "format": "online"
}
string = json.dumps(session)
print(f'dict to json:{session}')
data = json.loads(string)
print(f'json to dict:{data}')
print(type(data))

# Exercise 17: CSV to JSON 

import csv
import json

data = []

with open("scores.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        data.append(row)

with open("scores.json", "w") as f:
    json.dump(data, f, indent=4)




