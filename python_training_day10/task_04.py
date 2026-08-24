# Create charts to communicate insights
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
data = {
    "name": [
        "Arun", "Bala", "Charan", "David", "Elan",
        "Fahad", "Ganesh", "Hari", "Ishan", "John",
        "Kiran", "Lokesh", "Manoj", "Naveen", "Prakash"
    ],
 
    "department": [
        "IT", "HR", "IT", "Finance", "HR",
        "IT", "Finance", "IT", "HR", "Finance",
        "IT", "HR", "Finance", "IT", "HR"
    ],
 
    "salary": [
        50000, 40000, 60000, 55000, 45000,
        70000, 65000, 52000, 48000, 58000,
        75000, 42000, 62000, 68000, 46000
    ],
 
    "years_experience": [
        2, 3, 4, 5, 3,
        6, 5, 4, 2, 4,
        7, 3, 6, 5, 2
    ]
}
 
df = pd.DataFrame(data)
 
 
average_salary = df.groupby("department")["salary"].mean()
 
average_salary.plot(kind="bar")
 
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
 
plt.show()
 
sns.scatterplot(
    data=df,
    x="years_experience",
    y="salary",
    hue="department"
)
 
plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
 
plt.show()
 
 
plt.hist(df["salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
 
plt.show()