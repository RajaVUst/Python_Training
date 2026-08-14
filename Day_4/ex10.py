def print_student_info(**details):
    print(details)
    for key,value in details.items():
        print(f"{key}:{value}")

print_student_info(name='s', age=20, course='B.Tech', city='Bengaluru')
print_student_info(name='v', age=20, course='B.Tech', city='Bengaluru')
print_student_info(name='e', age=20, course='B.Tech', city='Bengaluru')

#Output

"""
{'name': 's', 'age': 20, 'course': 'B.Tech', 'city': 'Bengaluru'}
name:s
age:20
course:B.Tech
city:Bengaluru
{'name': 'v', 'age': 20, 'course': 'B.Tech', 'city': 'Bengaluru'}
name:v
age:20
course:B.Tech
city:Bengaluru
{'name': 'e', 'age': 20, 'course': 'B.Tech', 'city': 'Bengaluru'}
name:e
age:20
course:B.Tech
city:Bengaluru
"""