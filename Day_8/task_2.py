# Task 2.1 — Student Grade Book

students = {
    "alice": [88, 92, 79],
    "bob":   [65, 70, 68],
    "carol": [95, 91, 89],
}

averages = {
    name: (sum(grades) / len(grades) if grades else 0)

for name, grades in students.items()
}
above_80 = {name for name, grades in students.items()
if grades and all(grade > 80 for grade in grades)
}
sorted_students = sorted(averages.items(),
key=lambda item: item[1],

reverse=True
)
print("Averages:", averages)
print("All grades > 80:", above_80)
print("Sorted by average:", sorted_students)

# output 

# Averages: {'alice': 86.33333333333333, 'bob': 67.66666666666667, 'carol': 91.66666666666667}
# All grades > 80: {'carol'}
# Sorted by average: [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667)]

# Task 2.2 — Set Operations: Access Control

team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}
common = team_a & team_b
unique_to_a = team_a - team_b
combined = team_a | team_b
symmetric_difference = team_a ^ team_b

print("Common:", common)
print("Unique to Team A:", unique_to_a)
print("Combined:", combined)
print("Symmetric Difference:", symmetric_difference)

# Output 

# Common: {'slack', 'jira'}
# Unique to Team A: {'github', 'figma'}
# Combined: {'notion', 'slack', 'figma', 'github', 'jira', 'vscode'}
# Symmetric Difference: {'notion', 'figma', 'github', 'vscode'}

#Task 2.3 — Mutability Trap

# default arguments are evaluated only once, when the function is defined, not each time it is called.
#The list basket=[] is a mutable object. Every call that doesn't provide a basket argument uses the same list object, so items keep accumulating.

def add_item(item, basket=None):
    if basket is None:
        basket = []

    basket.append(item)
    return basket


print(add_item("apple"))
print(add_item("banana"))


def update_settings(key, value, settings={}):
    settings[key] = value
    return settings

print(update_settings("theme", "dark"))
print(update_settings("language", "en"))