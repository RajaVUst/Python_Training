import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read employees data from CSV
employees = pd.read_csv("employees.csv")


# 1. BAR CHART - Average Salary Across Departments

average_salary = employees.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
average_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Question:
# This chart answers: "How does the average salary compare across departments?"


# 2. SCATTER PLOT - Years of Experience vs Salary

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
plt.ylabel("Salary")

plt.tight_layout()
plt.show()

# Question:
# This chart answers: "What relationship exists between years of experience and salary?"


# 3. HISTOGRAM - Salary Distribution

plt.figure(figsize=(8, 5))

plt.hist(
    employees["salary"],
    bins=8,
    edgecolor="black"
)

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()

# Question:
# This chart answers: "How are employee salaries distributed across different salary ranges?"


# 4. STRETCH GOAL - LINE CHART

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]

headcount = [20, 22, 24, 27, 29, 32, 35, 38]

plt.figure(figsize=(8, 5))

plt.plot(months, headcount, marker="o")

plt.title("Monthly Employee Headcount Growth")
plt.xlabel("Month")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()

# Explanation:
# A line chart is better for showing trends because it clearly shows
# how a value changes over time and the direction of the trend.