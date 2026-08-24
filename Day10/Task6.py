# Day 10 - Task 6
from Day10.Task2 import employees


#1A
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"{self.name}:{self.price}"

product=Product(' Price of Laptop is',98000)
print(product)

#1B fastapi

#1c
summary = (
    employees
    .groupby("department")
    .agg(
        average_salary=("salary", "mean"),
        headcount=("name", "count")
    )
)

print(summary)



#output
'''
CSV file created successfully.
Employee DataFrame:
           name   department  salary  years_experience
0           Sai  Engineering   85000                 3
1           ram           HR   52000                 2
2       Krishna        Sales   61000                 4
3        athira  Engineering   92000                 6
4     aishwarya      Finance   73000                 5
5        Ananya        Sales   65000                 3
6        Vikram  Engineering  105000                 8
7          Isha           HR   56000                 4
8         Arjun      Finance   78000                 6
9         Nisha        Sales   68000                 5
10        Rahul  Engineering   88000                 4
11        Priya      Finance   81000                 7
12        Kiran           HR   59000                 5
13        Sneha        Sales   72000                 6
14         Deva  Engineering   98000                 7
15  Devika Tara        Legal   70000                 3

DataFrame information:
<class 'pandas.DataFrame'>
RangeIndex: 16 entries, 0 to 15
Data columns (total 4 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   name              16 non-null     str  
 1   department        16 non-null     str  
 2   salary            16 non-null     int64
 3   years_experience  16 non-null     int64
dtypes: int64(2), str(2)
memory usage: 644.0 bytes

Statistical summary:
              salary  years_experience
count      16.000000         16.000000
mean    75187.500000          4.875000
std     15406.573272          1.707825
min     52000.000000          2.000000
25%     64000.000000          3.750000
50%     72500.000000          5.000000
75%     85750.000000          6.000000
max    105000.000000          8.000000

Engineering employees using boolean indexing:
      name   department  salary  years_experience
0      Sai  Engineering   85000                 3
3   athira  Engineering   92000                 6
6   Vikram  Engineering  105000                 8
10   Rahul  Engineering   88000                 4
14    Deva  Engineering   98000                 7

Engineering employees using query:
      name   department  salary  years_experience
0      Sai  Engineering   85000                 3
3   athira  Engineering   92000                 6
6   Vikram  Engineering  105000                 8
10   Rahul  Engineering   88000                 4
14    Deva  Engineering   98000                 7

Are both filtering results identical? True

Department summary:
             average_salary  headcount
department                            
Engineering    93600.000000          5
Finance        77333.333333          3
HR             55666.666667          3
Legal          70000.000000          1
Sales          66500.000000          4

Departments sorted by average salary:
             average_salary  headcount
department                            
Engineering    93600.000000          5
Finance        77333.333333          3
Legal          70000.000000          1
Sales          66500.000000          4
HR             55666.666667          3
 Price of Laptop is:98000
             average_salary  headcount
department                            
Engineering    93600.000000          5
Finance        77333.333333          3
HR             55666.666667          3
Legal          70000.000000          1
Sales          66500.000000          4

Process finished with exit code 0
'''