
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# TASK 1


prices = [
    10, 20, 25, 30, 35,
    40, 45, 50, 55, 60,
    65, 70, 75, 80, 85,
    90, 95, 100, 120, 150
]

taxed_prices_loop = []

for price in prices:
    taxed_price = price * 1.08
    taxed_prices_loop.append(taxed_price)

print("Loop-based prices:")
print(taxed_prices_loop)


prices_array = np.array(prices)

taxed_prices_numpy = prices_array * 1.08

print("\nNumPy vectorized prices:")
print(taxed_prices_numpy)


print("\nBoth versions are identical:")
print(np.allclose(taxed_prices_loop, taxed_prices_numpy))
# Output: True

threshold = 50

above_threshold = taxed_prices_numpy[taxed_prices_numpy > threshold]

print("\nTaxed prices above 50:")
print(above_threshold)

numbers = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

row_sums = numbers.sum(axis=1)
column_sums = numbers.sum(axis=0)

print("\n2D array:")
print(numbers)

print("Row sums:")
print(row_sums)
# Output: [10 26 42]

print("Column sums:")
print(column_sums)
# Output: [15 18 21 24]


# TASK 2 

employees_data = {
    "name": [
        "Amit", "Reni", "Tara", "John", "David",
        "Priya", "Rahul", "Sneha", "Arun", "Meera",
        "Vijay", "Anu", "Kiran", "Neha", "Suresh"
    ],

    "department": [
        "IT", "HR", "Finance", "IT", "Marketing",
        "IT", "HR", "Finance", "Marketing", "IT",
        "Finance", "HR", "Marketing", "IT", "Finance"
    ],

    "salary": [
        60000, 50000, 65000, 72000, 55000,
        80000, 52000, 70000, 58000, 75000,
        68000, 54000, 62000, 85000, 73000
    ],

    "years_experience": [
        3, 2, 5, 6, 3,
        8, 2, 6, 4, 7,
        5, 3, 4, 9, 7
    ]
}


employees = pd.DataFrame(employees_data)

employees.to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv")

print("\nDataFrame info:")
print(df.info())

print("\nDataFrame description:")
print(df.describe())

it_employees_boolean = df[df["department"] == "IT"]

print("\nIT employees using boolean indexing:")
print(it_employees_boolean)


it_employees_query = df.query("department == 'IT'")

print("\nIT employees using query():")
print(it_employees_query)


print("\nBoth filtering approaches give the same result:")
print(it_employees_boolean.equals(it_employees_query.reset_index(drop=True)))


print(
    it_employees_boolean.reset_index(drop=True).equals(
        it_employees_query.reset_index(drop=True)
    )
)
# Output: True

department_summary = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    headcount=("name", "count")
)

department_summary = department_summary.sort_values(
    "average_salary",
    ascending=False
)


print("\nDepartment summary:")
print(department_summary)


# TASK 3 - JOIN THE DATA

departments = pd.DataFrame({
    "department": [
        "IT",
        "HR",
        "Finance"
    ],

    "department_budget": [
        500000,
        250000,
        350000
    ]
})


print("\nDepartments:")
print(departments)


inner_join = pd.merge(
    df,
    departments,
    on="department",
    how="inner"
)


print("\nInner join:")
print(inner_join)


new_employee = pd.DataFrame({
    "name": ["Karthik"],
    "department": ["Operations"],
    "salary": [60000],
    "years_experience": [4]
})


df_with_new_employee = pd.concat(
    [df, new_employee],
    ignore_index=True
)



left_join = pd.merge(
    df_with_new_employee,
    departments,
    on="department",
    how="left"
)


print("\nLeft join:")
print(left_join)




df_with_missing = df.copy()

df_with_missing.loc[2, "salary"] = np.nan
df_with_missing.loc[5, "years_experience"] = np.nan


print("\nMissing values:")
print(df_with_missing.isna().sum())


df_with_missing["salary"] = df_with_missing["salary"].fillna(
    df_with_missing["salary"].mean()
)


df_with_missing["years_experience"] = df_with_missing[
    "years_experience"
].fillna(
    df_with_missing["years_experience"].mean()
)


print("\nData after handling missing values:")
print(df_with_missing)


df = df_with_missing


# TASK 4 - TELL A STORY

print("\n================ TASK 4 ================")



average_salary = df.groupby("department")["salary"].mean()

plt.figure()

average_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()


plt.figure()

for department in df["department"].unique():

    department_data = df[df["department"] == department]

    plt.scatter(
        department_data["years_experience"],
        department_data["salary"],
        label=department
    )

plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()

plt.tight_layout()
plt.show()



plt.figure()

plt.hist(df["salary"], bins=6)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()



# TASK 5 

print("\n================ TASK 5 ================")

print("""
1. Java habits I had to adjust:

OOP:
In Java, I am used to strict access modifiers such as private,
protected and public. In Python, encapsulation is based more on
conventions such as _protected and name-mangling for __private.

FastAPI/testing:
In Java, I am used to writing more explicit classes and validation
code. With FastAPI and Pydantic, request validation can be handled
directly through Pydantic models.

Pandas/NumPy:
In Java, I would normally use loops to process elements. With
NumPy and Pandas, I need to think more about vectorized operations,
boolean filtering, grouping and DataFrame operations instead.


2. Skill I expect to see again:

I expect to use Pandas DataFrame filtering and grouping again in
the upcoming ML modules. Before training a machine learning model,
data usually needs to be explored, filtered, cleaned and summarized.
Pandas provides useful operations for preparing that data before
passing it to a model.


3. Least confident topic:

My least confident topic is NumPy broadcasting and vectorized
operations. To improve, I will practice small NumPy examples
involving arrays, boolean masking, broadcasting and axis-based
operations before the readiness assessment.
""")

# TASK 6

print("\n================ TASK 6 ================")

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Joel")

print("\nClass example:")
print(student)
# Output: Joel


from fastapi import FastAPI
from pydantic import BaseModel


class StudentRequest(BaseModel):

    name: str
    age: int


app = FastAPI()


@app.post("/students")
def create_student(student: StudentRequest):

    return {
        "name": student.name,
        "age": student.age
    }


# Request:
# {
#     "name": "Joel",
#     "age": 23
# }
#
# Response:
# {
#     "name": "Joel",
#     "age": 23
# }

summary = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    headcount=("name", "count")
)

print("\nPandas groupby().agg() example:")
print(summary)

print("""
SELF-CHECK:

1. Class:
   Constructor: __init__()
   Dunder method: __str__()

2. FastAPI:
   Pydantic BaseModel defines the request structure.
   @app.post() defines the endpoint.

3. Pandas:
   groupby() groups rows by department.
   agg() calculates average salary and headcount.
""")
