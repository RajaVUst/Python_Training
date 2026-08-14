def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(name="Aron", age=21, course="Python", city="Trivandrum")

'''
OUTPUT:
name: Aron
age: 21
course: Python
city: Trivandrum
'''