import csv

with open("employee.csv","w",newline="") as f:
    writer=csv.writer(f)
    
    writer.writerow(["Name","Dept","Salary"])
    writer.writerow(["Bonny","Fresher",28000])
    writer.writerow(["Vinaya","Fresher",28000])
    writer.writerow(["Arjun","Fresher",28000])
    writer.writerow(["Ezbon","Fresher",28000])
    writer.writerow(["Ashbin","Fresher",28000])
    
with open ("employee.csv","r",newline="") as f:
    reader=csv.DictReader(f)
    reverse_order=list(reader)
    
    for employee in reversed(reverse_order):
        print(employee)
        
        
# OUTPUT

# {'Name': 'Ashbin', 'Dept': 'Fresher', 'Salary': '28000'}
# {'Name': 'Ezbon', 'Dept': 'Fresher', 'Salary': '28000'}
# {'Name': 'Arjun', 'Dept': 'Fresher', 'Salary': '28000'}
# {'Name': 'Vinaya', 'Dept': 'Fresher', 'Salary': '28000'}
# {'Name': 'Bonny', 'Dept': 'Fresher', 'Salary': '28000'}
