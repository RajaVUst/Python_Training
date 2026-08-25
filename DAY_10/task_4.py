# Task 4 - Tell a Story
# Visualization: bar chart, scatter plot, histogram, stretch: line chart
# Charts are saved as PNG files in the DAY_10 folder.

import pandas as pd
import matplotlib
matplotlib.use("Agg")           # non-interactive backend — saves to file without needing a GUI
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

# ─── 1. Bar chart — avg salary per department ─────────────────────────────────
# QUESTION answered: Which department pays the MOST on average? (comparison between groups)
avg_salary = df.groupby("department")["salary"].mean().sort_values(ascending=False)

plt.figure(figsize=(7, 4))
avg_salary.plot(kind="bar", color=["steelblue", "salmon", "seagreen"])
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_1_bar.png")
plt.close()
print("Saved: chart_1_bar.png")

# ─── 2. Scatter plot — years_experience vs salary, colored by department ──────
# QUESTION answered: Is there a RELATIONSHIP between experience and salary, and does it differ by department?
colors = {"Engineering": "steelblue", "Marketing": "salmon", "HR": "seagreen"}

plt.figure(figsize=(7, 4))
for dept, group in df.groupby("department"):
    plt.scatter(group["years_experience"], group["salary"],
                label=dept, color=colors[dept], s=80)

plt.title("Experience vs Salary by Department")
plt.xlabel("Years of Experience")
plt.ylabel("Salary ($)")
plt.legend()
plt.tight_layout()
plt.savefig("chart_2_scatter.png")
plt.close()
print("Saved: chart_2_scatter.png")

# ─── 3. Histogram — salary distribution ──────────────────────────────────────
# QUESTION answered: How are salaries DISTRIBUTED — are they spread out or clustered?
plt.figure(figsize=(7, 4))
plt.hist(df["salary"], bins=6, color="mediumpurple", edgecolor="white")
plt.title("Salary Distribution")
plt.xlabel("Salary ($)")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("chart_3_histogram.png")
plt.close()
print("Saved: chart_3_histogram.png")

# ─── Stretch: Line chart — monthly headcount growth trend ─────────────────────
# QUESTION answered: How does headcount change OVER TIME? A line fits a trend
# better than a bar chart because it visually emphasises direction and continuity.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
headcount = [10, 12, 13, 15, 18, 20]

plt.figure(figsize=(7, 4))
plt.plot(months, headcount, marker="o", color="darkorange", linewidth=2)
plt.title("Monthly Headcount Growth")
plt.xlabel("Month")
plt.ylabel("Headcount")
plt.tight_layout()
plt.savefig("chart_4_line.png")
plt.close()
print("Saved: chart_4_line.png")
