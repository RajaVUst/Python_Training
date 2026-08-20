# Task 2.1 - Student Grade Book
students = {"alice" : [88, 92, 79], "bob": [65, 70, 68], "carol": [95,91,89], "annie": []}
avg_grade = {student:sum(scores)/len(scores) if scores else 0 for student, scores in students.items()}
toppers = {stu for stu, grade in avg_grade.items() if grade> 80}
notice = sorted(avg_grade.items(), key = lambda i:i[1], reverse = True)
print(avg_grade)    # {'alice': 86.33333333333333, 'bob': 67.66666666666667, 'carol': 91.66666666666667, 'annie': 0}
print(toppers)  # {'alice', 'carol'}
print(notice)   # [('carol', 91.66666666666667), ('alice', 86.33333333333333), ('bob', 67.66666666666667), ('annie', 0)]

# Task 2.2 - Set Operations: Access Control
team_a = {"figma","jira","slack","github"}
team_b = {"jira","slack","notion","vscode"}
common = team_a & team_b
unique = team_a - team_b
combined = team_a | team_b
sym_diff = team_a ^ team_b

def access_report(team_a,team_b):
    return {
        "common" : team_a & team_b,
        "unique" : team_a - team_b,
        "combined" : team_a | team_b,
        "sym_diff" : team_a ^ team_b
    }
print(access_report(team_a,team_b))
# {'common': {'slack', 'jira'}, 'unique': {'figma', 'github'}, 'combined': {'slack', 'notion', 'vscode', 'github', 'jira', 'figma'}, 'sym_diff': {'notion', 'vscode', 'github', 'figma'}}

# Task 2.3 - Mutability Trap
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item("apple"))    # ['apple']
print(add_item("banana"))   # ['banana']

def toll(vehicle, vehicles_passed = {}):
    vehicles_passed[vehicle] = len(vehicles_passed)+1
    return vehicles_passed

print(toll("Creta"))    # {'Creta': 1}
print(toll("Innova"))   # {'Creta': 1, 'Innova': 2}
