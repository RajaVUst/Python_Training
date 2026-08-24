# Task 4: Data Visualization with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

employees = pd.DataFrame({
    "department": ["IT", "HR", "Finance", "IT", "HR", "Finance"],
    "salary": [60000, 50000, 70000, 65000, 52000, 72000],
    "years_experience": [3, 2, 6, 5, 4, 7]
})

avg_salary = employees.groupby("department")["salary"].mean()

avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

colors = {
    "IT": "blue",
    "HR": "green",
    "Finance": "red"
}

for dept in employees["department"].unique():
    subset = employees[employees["department"] == dept]

    plt.scatter(
        subset["years_experience"],
        subset["salary"],
        label=dept,
        color=colors[dept]
    )

plt.title("Experience vs Salary")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

plt.hist(employees["salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Bar Chart:
# Compares average salary between departments.

# Scatter Plot:
# Shows the relationship between years of experience and salary.

# Histogram:
# Shows how salaries are distributed across employees.

# Output:
# Bar chart displayed
# Scatter plot displayed
# Histogram displayed