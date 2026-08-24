# Day 10 - Task 2

import pandas as pd

# Create a DataFrame containing at least 15 employees
employee_data = {
    "name": [
        "Sai", "ram", "Krishna", "athira",
        "aishwarya", "Ananya", "Vikram", "Isha",
        "Arjun", "Nisha", "Rahul", "Priya",
        "Kiran", "Sneha", "Deva", "Devika Tara"
    ],

    "department": [
        "Engineering", "HR", "Sales", "Engineering",
        "Finance", "Sales", "Engineering", "HR",
        "Finance", "Sales", "Engineering", "Finance",
        "HR", "Sales", "Engineering", "Legal"
    ],

    "salary": [
        85000, 52000, 61000, 92000,
        73000, 65000, 105000, 56000,
        78000, 68000, 88000, 81000,
        59000, 72000, 98000, 70000
    ],

    "years_experience": [
        3, 2, 4, 6,
        5, 3, 8, 4,
        6, 5, 4, 7,
        5, 6, 7, 3
    ]
}

employees_df = pd.DataFrame(employee_data)

# Save the DataFrame as a CSV file
employees_df.to_csv("employees.csv", index=False)

print("CSV file created successfully.")



employees = pd.read_csv("employees.csv")

print("Employee DataFrame:")
print(employees)


# 1. DataFrame information
print("\nDataFrame information:")
employees.info()


# Statistical summary
print("\nStatistical summary:")
print(employees.describe())


# 2. Boolean indexing
engineering_boolean = employees[
    employees["department"] == "Engineering"
]

print("\nEngineering employees using boolean indexing:")
print(engineering_boolean)


# Using query()
engineering_query = employees.query(
    "department == 'Engineering'"
)

print("\nEngineering employees using query:")
print(engineering_query)


# Confirm both filtering methods return identical rows
print(
    "\nAre both filtering results identical?",
    engineering_boolean.equals(engineering_query)
)


# 3. Average salary and headcount by department
department_summary = (
    employees
    .groupby("department")
    .agg(
        average_salary=("salary", "mean"),
        headcount=("name", "count")
    )
)

print("\nDepartment summary:")
print(department_summary)


# 4. Sort in descending order
department_summary = department_summary.sort_values(
    by="average_salary",
    ascending=False
)

print("\nDepartments sorted by average salary:")
print(department_summary)




