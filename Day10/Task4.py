# Day 10 - Task 4


import matplotlib.pyplot as plt
import seaborn as sns

from Day10.Task3 import employees_clean

sns.set_theme(style="whitegrid")

#1. Average salary bar chart
average_salary = (
    employees_clean
    .groupby("department", as_index=False)
    .agg(
        average_salary=("salary", "mean")
    )
)

plt.figure(figsize=(9, 5))

sns.barplot(
    data=average_salary,
    x="department",
    y="average_salary",
    hue="department",
    legend=False
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# 2. Experience versus salary scatter plot


plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=employees_clean,
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

#3. Salary histogram

plt.figure(figsize=(9, 5))

sns.histplot(
    data=employees_clean,
    x="salary",
    bins=8,
    kde=True
)

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

#4.Stretch goal: line chart
monthly_growth = pd.DataFrame({
    "month": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June"
    ],

    "headcount": [
        16,
        17,
        17,
        19,
        21,
        24
    ]
})

plt.figure(figsize=(9, 5))

sns.lineplot(
    data=monthly_growth,
    x="month",
    y="headcount",
    marker="o"
)

plt.title("Monthly Headcount Growth")
plt.xlabel("Month")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

