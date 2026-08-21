# #1.1
# items = ["pen", "notebook", "pen", "eraser", "notebook", "pen", "stapler"]
# ariving_list=items
# first_batch=tuple(items[:3])
# unique_items=set(items)

# items_count={}
# for item in items:
#     if item in items_count:
#         items_count[item]+=1
#     else:
#         items_count[item]=1    

# print("Arrival List:", ariving_list)
# print("First Batch:", first_batch)
# print("Unique Items:", unique_items)
# print("Item Counts:", items_count)

#1.2

# squares=[i*i for i in range(1,21) if i%2==0 ]
# print(squares)
# word_lengths={word:len(word) for word in ["python", "java", "c", "kotlin"]}
# print(word_lengths)
# unique_vowels={ ch for ch in "the quick brown fox jumps over the lazy dog" if ch in 'aeiou'}
# print(unique_vowels)


#1.3
# sentences = ["the sky is blue", "python is fun", "list comprehensions are handy"]
# result=[word for sentence in sentences for word in sentence.split() if len(word)>2]
# print(result)
# unique_word={word.lower() for sentence in sentences for word in sentence.split()}
# print(unique_word)

#1.4
# students = {
#     "alice": [88, 92, 79],
#     "bob":   [65, 70, 68],
#     "carol": [95, 91, 89],
# }
# avg_studnet={ student: round(sum(grades)/len(grades), 2) if grades else 0 for student, grades in students.items()}

# unique_name={ student for student, grades in students.items()  if grades and   all(grade>80 for grade in grades) }

# highest_grade=sorted(avg_studnet.items(),key=lambda x:x[1], reverse=True)
# print("Average grades:", avg_studnet)
# print("Students with every grade above 80:", unique_name)
# print("Students sorted by average:", highest_grade)

# #1.5
# team_a = {"figma", "jira", "slack", "github"}
# team_b = {"jira", "slack", "notion", "vscode"}
# common = team_a & team_b
# only_a = team_a - team_b
# combined = team_a | team_b
# symmetric_difference = team_a ^ team_b
# print("Common tools:", common)
# print("Only Team A:", only_a)
# print("Combined tools:", combined)
# print("Symmetric difference:", symmetric_difference)


# def access_report(team_a, team_b):
#     return {
#         "common": team_a & team_b,
#         "only_a": team_a - team_b,
#         "combined": team_a | team_b,
#         "symmetric_difference": team_a ^ team_b
#     }

# report = access_report(team_a, team_b)

# print("Access Report:", report)


#1.6
# def add_item(item, basket=None):
#     if basket is None:
#         basket = []

#     basket.append(item)
#     return basket

# print(add_item("apple"))
# print(add_item("banana"))


# #1.7
# logs = [
#     "2026-08-20 10:00 INFO Application started",
#     "2026-08-20 10:05 INFO User logged in",
#     "2026-08-20 10:10 WARNING High memory usage",
#     "2026-08-20 10:15 ERROR Database connection failed",
#     "2026-08-20 10:20 INFO Application stopped"
# ]

# with open("log.txt", "w") as file:
#     for line in logs:
#         file.write(line + "\n")

# with open("log.txt", "r") as file:
#     for number, line in enumerate(file, start=1):
#         print(number, line.strip())

# file = open("log.txt", "r")

# for line in file:
#     print(line.strip())

# file.close()

# with open("log.txt", "a") as file:
#     file.write("2026-08-20 10:25 INFO New log entry\n")

  #1.8
    # import csv

    # employees = [
    #     ["Alice", "Engineering", 70000],
    #     ["Bob", "HR", 50000],
    #     ["Carol", "Engineering", 80000],
    #     ["David", "Sales", 60000],
    #     ["Eve", "HR", 55000]
    # ]

    # with open("employees.csv", "w", newline="") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["name", "department", "salary"])

    #     for employee in employees:
    #         writer.writerow(employee)


    # department_salary = {}

    # with open("employees.csv", "r", newline="") as file:
    #     reader = csv.DictReader(file)

    #     for employee in reader:
    #         print(employee)

    #         department = employee["department"]
    #         salary = int(employee["salary"])

    #         if department not in department_salary:
    #             department_salary[department] = 0

    #         department_salary[department] += salary

    # print("Total salary per department:")
    # print(department_salary)


    # with open("employees.csv", "r", newline="") as input_file:
    #     reader = csv.DictReader(input_file)

    #     with open("employees_updated.csv", "w", newline="") as output_file:
    #         fieldnames = ["name", "department", "salary"]

    #         writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    #         writer.writeheader()

    #         for employee in reader:
    #             salary = int(employee["salary"])

    #             if employee["department"] == "Engineering":
    #                 salary = round(salary * 1.10)

    #             employee["salary"] = salary

    #             writer.writerow(employee)