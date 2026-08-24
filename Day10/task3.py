import pandas as pd, numpy as np

depts_data = {'Dept': ['IT', 'HR', 'Marketing', 'Sales', 'Maintainance'],
              'department_budget': [800000, 500000, 400000, 200000, 300000]
             }
pd.DataFrame(depts_data).to_csv('departments.csv',index = False)
dfd = pd.read_csv('departments.csv')
dfe = pd.read_csv('employees.csv')

join = pd.merge(dfd,dfe, on='Dept', how= 'inner')
print(join)
"""         Dept  department_budget      Name  Salary  years_experience
0             IT             800000  Shabanam   30000                 1
1             IT             800000  Varshith   30000                 1
2             IT             800000  Varshith   30000                 1
3             HR             500000    Vinaya   35000                 1
4             HR             500000    Vinaya   35000                 1
5             HR             500000    Vinaya   35000                 1
6      Marketing             400000     Arsha   25000                 2
7      Marketing             400000      Aish   25000                 2
8      Marketing             400000      Aish   25000                 2
9          Sales             200000      Ajay   40000                 2
10         Sales             200000      Ajay   40000                 2
11         Sales             200000      Ajay   40000                 2
12  Maintainance             300000  Prasanna   35000                 3
13  Maintainance             300000  Prasanna   35000                 3
14  Maintainance             300000  Prasanna   35000                 3  """

new_emp = pd.DataFrame({'Name': ['Rahul'], 'Dept': ['Finance'], 'Salary': [450000], 'years_experience':[4]})

employees = pd.concat([dfe,new_emp], ignore_index = True)
print(employees)
left = pd.merge(employees, dfd, on = 'Dept', how = 'left')
print(left)
"""         Name          Dept  Salary  years_experience  department_budget
0   Shabanam            IT   30000                 1           800000.0
1     Vinaya            HR   35000                 1           500000.0
2      Arsha     Marketing   25000                 2           400000.0
3       Ajay         Sales   40000                 2           200000.0
4   Prasanna  Maintainance   35000                 3           300000.0
5   Varshith            IT   30000                 1           800000.0
6     Vinaya            HR   35000                 1           500000.0
7       Aish     Marketing   25000                 2           400000.0
8       Ajay         Sales   40000                 2           200000.0
9   Prasanna  Maintainance   35000                 3           300000.0
10  Varshith            IT   30000                 1           800000.0
11    Vinaya            HR   35000                 1           500000.0
12      Aish     Marketing   25000                 2           400000.0
13      Ajay         Sales   40000                 2           200000.0
14  Prasanna  Maintainance   35000                 3           300000.0
15     Rahul       Finance  450000                 4                NaN     """

employees.loc[2, 'Salary'] = np.nan
employees.loc[5, 'Salary'] = np.nan

employees.loc[7, 'years_experience'] = np.nan
employees.loc[10, 'years_experience'] = np.nan

print(employees.isna().sum())
""" 
Name                0
Dept                0
Salary              2
years_experience    2
dtype: int64    """

employees['Salary'] = employees['Salary'].fillna(employees['Salary'].mean())
employees['years_experience'] = employees['years_experience'].fillna(employees['years_experience'].mean())

print(employees)
"""         
Name          Dept         Salary  years_experience
0   Shabanam            IT   30000.000000               1.0
1     Vinaya            HR   35000.000000               1.0
2      Arsha     Marketing   63571.428571               2.0
3       Ajay         Sales   40000.000000               2.0
4   Prasanna  Maintainance   35000.000000               3.0
5   Varshith            IT   63571.428571               1.0
6     Vinaya            HR   35000.000000               1.0
7       Aish     Marketing   25000.000000               2.0
8       Ajay         Sales   40000.000000               2.0
9   Prasanna  Maintainance   35000.000000               3.0
10  Varshith            IT   30000.000000               2.0
11    Vinaya            HR   35000.000000               1.0
12      Aish     Marketing   25000.000000               2.0
13      Ajay         Sales   40000.000000               2.0
14  Prasanna  Maintainance   35000.000000               3.0
15     Rahul       Finance  450000.000000               4.0
"""