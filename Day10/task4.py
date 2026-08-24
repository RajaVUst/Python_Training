import matplotlib.pyplot as plt
import seaborn as sns, pandas as pd

from task3 import employees

sns.set_theme(style="whitegrid")

average_salary = (
    employees
    .groupby("Dept", as_index=False)
    .agg(
        average_salary=("Salary", "mean")
    )
)

plt.figure(figsize=(9, 5))

sns.barplot(
    data=average_salary,
    x="Dept",
    y="average_salary",
    hue="Dept",
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
    data=employees
,
    x="years_experience",
    y="Salary",
    hue="Dept",
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
    data=employees
,
    x="Salary",
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