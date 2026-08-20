# Task 2.1 - Student Grade Book

students = {
    "alice": [88, 92, 79],
    "bob": [65, 70, 68],
    "carol": [95, 91, 89],
    "david": []
}
average_grades = {
    name: (sum(grades) / len(grades) if grades else 0)
    for name, grades in students.items()
}
top_students = {
    name
    for name, grades in students.items()
    if grades and all(grade > 80 for grade in grades)
}
sorted_students = sorted(
    average_grades.items(),
    key=lambda x: x[1],
    reverse=True
)
print("Average Grades:", average_grades)
print("Students with all grades above 80:", top_students)
print("Sorted Students:", sorted_students)
# Output:
# Average Grades: {'alice': 86.33333333333333,
#                  'bob': 67.66666666666667,
#                  'carol': 91.66666666666667,
#                  'david': 0}
# Students with all grades above 80: {'carol'}
# Sorted Students: [('carol', 91.66666666666667),
#                   ('alice', 86.33333333333333),
#                   ('bob', 67.66666666666667),
#                   ('david', 0)]


# Task 2.2 - Set Operations: Access Control
team_a = {"figma", "jira", "slack", "github"}
team_b = {"jira", "slack", "notion", "vscode"}
common_tools = team_a & team_b
print("Common Tools:", common_tools)
unique_to_a = team_a - team_b
print("Unique to Team A:", unique_to_a)
combined_tools = team_a | team_b
print("Combined Toolset:", combined_tools)
symmetric_difference = team_a ^ team_b
print("Symmetric Difference:", symmetric_difference)
def access_report(team_a, team_b):
    return {
        "common": team_a & team_b,
        "unique_to_a": team_a - team_b,
        "combined": team_a | team_b,
        "symmetric_difference": team_a ^ team_b
    }
print("Access Report:", access_report(team_a, team_b))
# output:
"""
Common Tools: {'jira', 'slack'}
Unique to Team A: {'figma', 'github'}
Combined Toolset: {'figma', 'github', 'notion', 'jira', 'vscode', 'slack'}
Symmetric Difference: {'figma', 'github', 'notion', 'vscode'}
Access Report: {'common': {'jira', 'slack'}, 'unique_to_a': {'figma', 'github'}, 'combined': {'figma', 'github', 'notion', 'jira', 'vscode', 'slack'}, 'symmetric_difference': {'figma', 'github', 'notion', 'vscode'}}"""


# Task 2.3 - Mutability Trap
def add_item(item, basket=[]):
    basket.append(item)
    return basket
print(add_item("apple"))
print(add_item("banana"))
def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
def add_task(task, task_list=[]):
    task_list.append(task)
    return task_list
print(add_task("Study Python"))
print(add_task("Practice Sets"))
#output:
"""['apple'].
['apple', 'banana']
['apple']
['banana']
['Study Python']
['Study Python', 'Practice Sets']"""
