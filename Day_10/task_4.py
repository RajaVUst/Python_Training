import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --------------------------------------------------
# Employee Data
# --------------------------------------------------
employees = pd.DataFrame({
    "name": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Karen", "Leo", "Maria", "Nathan", "Olivia"
    ],
    "department": [
        "IT", "HR", "Finance", "IT", "HR",
        "Finance", "IT", "Sales", "Sales", "HR",
        "Finance", "IT", "Sales", "Finance", "HR"
    ],
    "salary": [
        75000, 55000, np.nan, 82000, 60000,
        72000, 78000, 65000, 69000, 58000,
        74000, 85000, 71000, 76000, 62000
    ],
    "years_experience": [
        5, 3, 4, 7, 2,
        6, 5, np.nan, 3, 2,
        7, 8, 5, 6, 4
    ]
})

# Handle missing values using column mean
employees["salary"] = employees["salary"].fillna(
    employees["salary"].mean()
)
employees["years_experience"] = employees["years_experience"].fillna(
    employees["years_experience"].mean()
)

# --------------------------------------------------
# 1. Bar Chart: Average Salary by Department
# --------------------------------------------------
avg_salary = (
    employees.groupby("department")["salary"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar", color="steelblue")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary ($)")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 2. Scatter Plot: Experience vs Salary
# --------------------------------------------------
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=employees,
    x="years_experience",
    y="salary",
    hue="department",
    s=100
)
plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 3. Histogram: Salary Distribution
# --------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(
    employees["salary"],
    bins=6,
    color="orange",
    edgecolor="black"
)
plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary ($)")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# Stretch Goal: Monthly Headcount Trend
# --------------------------------------------------
headcount_growth = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Headcount": [12, 13, 14, 14, 15, 16]
})

plt.figure(figsize=(8, 5))
plt.plot(
    headcount_growth["Month"],
    headcount_growth["Headcount"],
    marker="o",
    linewidth=2
)
plt.title("Monthly Headcount Growth")
plt.xlabel("Month")
plt.ylabel("Number of Employees")
plt.grid(True)
plt.tight_layout()
plt.show()