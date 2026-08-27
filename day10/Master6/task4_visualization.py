import os

os.environ["MPLCONFIGDIR"] = ".matplotlib"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

employees = pd.read_csv("employees.csv")

average_salary = employees.groupby("department")["salary"].mean().sort_values()
average_salary.plot(kind="bar", color="steelblue")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("average_salary_bar.png")
plt.close()


sns.scatterplot(data=employees, x="years_experience", y="salary", hue="department")
plt.title("Experience and Salary by Department")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("experience_salary_scatter.png")
plt.close()

plt.hist(employees["salary"], bins=6, color="orange", edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("salary_histogram.png")
plt.close()


print("Three charts saved successfully")


# OUTPUT

# Three charts saved successfully
