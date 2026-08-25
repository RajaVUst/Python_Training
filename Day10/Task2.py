import pandas as pd

# --------------------------------------------------
# 1. Create employee data
# --------------------------------------------------

employees_data = {
    "name": [
        "Amit", "Rahul", "Priya", "Neha", "Arjun",
        "Sneha", "Vikram", "Pooja", "Rohan", "Anjali",
        "Karan", "Meera", "Raj", "Simran", "Dev"
    ],

    "department": [
        "IT", "IT", "HR", "HR", "Finance",
        "Finance", "IT", "Sales", "Sales", "HR",
        "Finance", "IT", "Sales", "Finance", "IT"
    ],

    "salary": [
        60000, 70000, 50000, 55000, 75000,
        80000, 65000, 45000, 50000, 52000,
        85000, 72000, 48000, 78000, 68000
    ],

    "years_experience": [
        2, 4, 3, 5, 6,
        7, 3, 2, 4, 3,
        8, 5, 2, 7, 4
    ]
}

employees_df = pd.DataFrame(employees_data)

# Save as CSV
employees_df.to_csv("employees.csv", index=False)


# --------------------------------------------------
# 2. Read CSV
# --------------------------------------------------

employees = pd.read_csv("employees.csv")

print(employees)


# Output:
#       name department  salary  years_experience
# 0     Amit         IT   60000                 2
# 1    Rahul         IT   70000                 4
# 2    Priya         HR   50000                 3
# ...
# 14     Dev         IT   68000                 4


print("\nDataFrame information:")
employees.info()


# Output:
# Information about columns, data types,
# non-null values, and memory usage is displayed.


print("\nStatistical description:")
print(employees.describe())


# Output:
#        salary  years_experience
# count    15.0              15.0
# mean  ...
# std   ...
# min   ...
# max   ...


# --------------------------------------------------
# 3. Filtering using boolean indexing
# --------------------------------------------------

it_boolean = employees[employees["department"] == "IT"]

print("\nIT employees using boolean indexing:")
print(it_boolean)


# --------------------------------------------------
# 4. Filtering using query()
# --------------------------------------------------

it_query = employees.query("department == 'IT'")

print("\nIT employees using query():")
print(it_query)


# Check both approaches give same rows
print("\nBoth filtering methods same:")
print(it_boolean.equals(it_query))


# Output:
# Both filtering methods same:
# True


# --------------------------------------------------
# 5. Groupby + aggregation
# --------------------------------------------------

department_summary = (
    employees
    .groupby("department")
    .agg(
        average_salary=("salary", "mean"),
        headcount=("name", "count")
    )
    .sort_values("average_salary", ascending=False)
)

print("\nDepartment summary:")
print(department_summary)


# Output:
#             average_salary  headcount
# department
# Finance          ...
# IT               ...
# HR               ...
# Sales            ...