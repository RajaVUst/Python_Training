def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(
    name="Saikiran",
    age=23,
    course="Python",
    city="Hyderabad"
)

'''
output
name: Saikiran
age: 23
course: Python
city: Hyderabad

'''