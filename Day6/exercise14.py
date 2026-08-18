import csv
import json

# Exercise 14
with open("profile.json", "r") as f:
    profile = json.load(f)

print("Name:", profile["name"])
print("Completed days:", len(profile["completed_days"]))

#output
'''
Name: Saikiran
Completed days: 5
'''