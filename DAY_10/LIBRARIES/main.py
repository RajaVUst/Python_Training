# import numpy as np

# # 1. Python list of 20 product prices
# prices = [
#     10, 20, 30, 40, 50,
#     60, 70, 80, 90, 100,
#     15, 25, 35, 45, 55,
#     65, 75, 85, 95, 105
# ]

# # 2. Apply 8% tax using a loop
# taxed_prices_loop = []

# for price in prices:
#     taxed_prices_loop.append(price * 1.08)

# print("Loop-based result:")
# print(taxed_prices_loop)


# # 3. Apply 8% tax using NumPy vectorization
# prices_array = np.array(prices)

# taxed_prices_numpy = prices_array * 1.08

# print("\nNumPy vectorized result:")
# print(taxed_prices_numpy)




# # 4. Boolean masking
# threshold = 50

# above_threshold = taxed_prices_numpy[taxed_prices_numpy > threshold]

# print("\nTaxed prices above 50:")
# print(above_threshold)


# # 5. Create a 2D NumPy array
# data = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])

# print("\n2D Array:")
# print(data)
# row_sums = data.sum(axis=1)

# print("\nRow sums:")
# print(row_sums)
# column_sums = data.sum(axis=0)

# print("\nColumn sums:")
# print(column_sums)


#2
# import pandas as pd

# # 1. Create employee data
# data = {
#     "name": [
#         "Ravi", "Priya", "Arun", "Sneha", "Kiran",
#         "Anil", "Divya", "Rahul", "Meena", "Vijay",
#         "Pooja", "Suresh", "Neha", "Amit", "Kavya"
#     ],
#     "department": [
#         "IT", "HR", "IT", "Finance", "IT",
#         "HR", "Finance", "IT", "HR", "Finance",
#         "IT", "HR", "Finance", "IT", "HR"
#     ],
#     "salary": [
#         60000, 50000, 75000, 65000, 80000,
#         55000, 70000, 72000, 52000, 68000,
#         90000, 58000, 62000, 85000, 60000
#     ],
#     "years_experience": [
#         3, 4, 6, 5, 8,
#         5, 7, 6, 3, 6,
#         10, 6, 4, 9, 7
#     ]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Save as CSV
# df.to_csv("employees.csv", index=False)


# # 2. Read CSV
# df = pd.read_csv("employees.csv")

# print("Employee Data:")
# print(df)


# # 3. Display information
# print("\nDataFrame Info:")
# df.info()


# # 4. Display statistics
# print("\nDataFrame Description:")
# print(df.describe())


# # 5. Filter IT department using Boolean indexing
# it_boolean = df[df["department"] == "IT"]

# print("\nIT Employees - Boolean Indexing:")
# print(it_boolean)


# # 6. Filter IT department using query()
# it_query = df.query("department == 'IT'")

# print("\nIT Employees - query():")
# print(it_query)


# # 8. Group by department and calculate
# # Average salary and headcount
# summary = (
#     df.groupby("department")
#       .agg(
#           average_salary=("salary", "mean"),
#           headcount=("name", "count")
#       )
#       .reset_index()
# )

# print("\nDepartment Summary:")
# print(summary)


# # 9. Sort by average salary in descending order
# summary = summary.sort_values(
#     "average_salary",
#     ascending=False
# )

# print("\nFinal Summary - Sorted by Average Salary:")
# print(summary)



#3
# import pandas as pd
# import numpy as np

# employees = pd.DataFrame({
#     "name": [
#         "Ravi", "Priya", "Arun", "Sneha", "Kiran",
#         "Anil", "Divya", "Rahul", "Meena", "Vijay",
#         "Pooja", "Suresh", "Neha", "Amit", "Kavya", "Raj"
#     ],
#     "department": [
#         "IT", "HR", "IT", "Finance", "IT",
#         "HR", "Finance", "IT", "HR", "Finance",
#         "IT", "HR", "Finance", "IT", "HR", "Marketing"
#     ],
#     "salary": [
#         60000, 50000, 75000, 65000, 80000,
#         55000, 70000, 72000, 52000, 68000,
#         90000, 58000, 62000, 85000, 60000, 55000
#     ],
#     "years_experience": [
#         3, 4, 6, 5, 8, 5, 7, 6,
#         3, 6, 10, 6, 4, 9, 7, 2
#     ]
# })

# departments = pd.DataFrame({
#     "department": ["IT", "HR", "Finance"],
#     "department_budget": [500000, 300000, 400000]
# })

# print("Employees:")
# print(employees)

# print("\nDepartments:")
# print(departments)

# inner_join = pd.merge(
#     employees,
#     departments,
#     on="department",
#     how="inner"
# )

# print("\nInner Join:")
# print(inner_join)

# left_join = pd.merge(
#     employees,
#     departments,
#     on="department",
#     how="left"
# )

# print("\nLeft Join:")
# print(left_join)

# employees.loc[2, "salary"] = np.nan
# employees.loc[7, "salary"] = np.nan

# print("\nEmployees with missing salaries:")
# print(employees)

# print("\nMissing values:")
# print(employees.isna().sum())

# # Fill missing salaries with the mean to keep all employee records.
# employees["salary"] = employees["salary"].fillna(
#     employees["salary"].mean()
# )

# print("\nEmployees after handling missing salaries:")
# print(employees)

# print("\nMissing values after handling:")
# print(employees.isna().sum())


#4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

employees = pd.DataFrame({
    "name": [
        "Ravi", "Priya", "Arun", "Sneha", "Kiran",
        "Anil", "Divya", "Rahul", "Meena", "Vijay",
        "Pooja", "Suresh", "Neha", "Amit", "Kavya",
        "Raj"
    ],
    "department": [
        "IT", "HR", "IT", "Finance", "IT",
        "HR", "Finance", "IT", "HR", "Finance",
        "IT", "HR", "Finance", "IT", "HR", "Marketing"
    ],
    "salary": [
        60000, 50000, 75000, 65000, 80000,
        55000, 70000, 72000, 52000, 68000,
        90000, 58000, 62000, 85000, 60000, 55000
    ],
    "years_experience": [
        3, 4, 6, 5, 8, 5, 7, 6,
        3, 6, 10, 6, 4, 9, 7, 2
    ]
})


# 1. Bar chart - Average salary by department

average_salary = employees.groupby("department")["salary"].mean()

average_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()




# 2. Scatter plot - Experience vs Salary

sns.scatterplot(
    data=employees,
    x="years_experience",
    y="salary",
    hue="department"
)

plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()


# 3. Histogram - Salary distribution

plt.hist(employees["salary"], bins=6)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

