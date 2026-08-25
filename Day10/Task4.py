from pathlib import Path
 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
 
employees = pd.read_csv(
    Path(__file__).resolve().parents[1] / "employees.csv"
)
 
# Average salary by department
avg_salary = (
    employees.groupby("department")["salary"]
    .mean()
    .reset_index()
)
 
# 1. Bar Chart
plt.figure(figsize=(6,4))
sns.barplot(data=avg_salary,
            x="department",
            y="salary")
 
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()
 
# 2. Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(
    data=employees,
    x="years_experience",
    y="salary",
    hue="department"
)
 
plt.title("Experience vs Salary")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.show()
 
# 3. Histogram
plt.figure(figsize=(6,4))
plt.hist(employees["salary"], bins=6)
 
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
 
# Stretch Goal
months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug"
]
 
headcount = [15, 16, 17, 18, 20, 21, 22, 24]
 
plt.figure(figsize=(7,4))
plt.plot(months, headcount, marker="o")
 
plt.title("Monthly Headcount Growth")
plt.xlabel("Month")
plt.ylabel("Headcount")
plt.show()
 