import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Employee data
employees = pd.DataFrame({
    "name": [
        "Amit", "Rahul", "Priya", "Neha",
        "Arjun", "Sneha", "Vikram", "Pooja",
        "Rohan", "Anjali", "Karan", "Meera",
        "Raj", "Simran", "Dev"
    ],

    "department": [
        "IT", "IT", "HR", "HR",
        "Finance", "Finance", "IT", "Sales",
        "Sales", "HR", "Finance", "IT",
        "Sales", "Finance", "IT"
    ],

    "salary": [
        60000, 70000, 50000, 55000,
        75000, 80000, 65000, 45000,
        50000, 52000, 85000, 72000,
        48000, 78000, 68000
    ],

    "years_experience": [
        2, 4, 3, 5,
        6, 7, 3, 2,
        4, 3, 8, 5,
        2, 7, 4
    ]
})


# --------------------------------------------------
# 1. Bar chart
# --------------------------------------------------

average_salary = (
    employees
    .groupby("department")["salary"]
    .mean()
)

average_salary.plot(
    kind="bar",
    title="Average Salary by Department"
)

plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()


# Question answered:
# "Which department has the highest or lowest average salary?"
# A bar chart is best for comparing values between categories.


# --------------------------------------------------
# 2. Scatter plot
# --------------------------------------------------

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


# Question answered:
# "Is there a relationship between years of experience
# and salary, and does that relationship differ by department?"
# A scatter plot is best for showing relationships between
# two numerical variables.


# --------------------------------------------------
# 3. Histogram
# --------------------------------------------------

plt.hist(
    employees["salary"],
    bins=6
)

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()


# Question answered:
# "How are salaries distributed across all employees?"
# A histogram is best for showing the distribution and
# frequency of numerical values.