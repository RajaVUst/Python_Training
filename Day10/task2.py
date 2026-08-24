import pandas as pd

data = {
    'Name': ['Shabanam', 'Vinaya', 'Arsha', 'Ajay', 'Prasanna', 'Varshith', 'Vinaya', 'Aish', 'Ajay', 'Prasanna', 'Varshith', 'Vinaya', 'Aish', 'Ajay', 'Prasanna'],
    'Dept': ['IT', 'HR', 'Marketing', 'Sales', 'Maintainance', 'IT', 'HR', 'Marketing', 'Sales', 'Maintainance', 'IT', 'HR', 'Marketing', 'Sales', 'Maintainance'],
    'Salary': [30000, 35000, 25000, 40000, 35000, 30000, 35000, 25000, 40000, 35000, 30000, 35000, 25000, 40000, 35000],
    'years_experience': [1, 1, 2, 2, 3, 1, 1, 2, 2, 3, 1, 1, 2, 2, 3]
}
pd.DataFrame(data).to_csv('employees.csv', index= False)

df = pd.read_csv('employees.csv')
print(df.info())
""" <class 'pandas.DataFrame'>
RangeIndex: 15 entries, 0 to 14
Data columns (total 4 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   Name              15 non-null     str  
 1   Dept              15 non-null     str  
 2   Salary            15 non-null     int64
 3   years_experience  15 non-null     int64
dtypes: int64(2), str(2)
memory usage: 612.0 bytes
None        """

print(df.describe())
"""              Salary  years_experience
count     15.000000         15.000000
mean   33000.000000          1.800000
std     5277.986629          0.774597
min    25000.000000          1.000000
25%    30000.000000          1.000000
50%    35000.000000          2.000000
75%    35000.000000          2.000000
max    40000.000000          3.000000   """

print("Indexing",df[df['Dept'] == 'Sales'])
""" Indexing     Name   Dept  Salary  years_experience
3   Ajay  Sales   40000                 2
8   Ajay  Sales   40000                 2
13  Ajay  Sales   40000                 2   
"""

print("Quering",df.query("Dept == 'Sales'"))
"""Quering     Name   Dept  Salary  years_experience
3   Ajay  Sales   40000                 2
8   Ajay  Sales   40000                 2
13  Ajay  Sales   40000     """

dept_group = df.groupby('Dept').agg(avg = ('Salary','mean'),headcount = ('Name','count'))
print(dept_group)
"""             avg  headcount
Dept                            
HR            35000.0          3
IT            30000.0          3
Maintainance  35000.0          3
Marketing     25000.0          3
Sales         40000.0          3    """

print(dept_group.sort_values(by = 'avg', ascending = False))
"""                   avg  headcount
Dept                            
Sales         40000.0          3
HR            35000.0          3
Maintainance  35000.0          3
IT            30000.0          3
Marketing     25000.0          3    
"""