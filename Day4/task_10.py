def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
print_student_info(
    name="Aiswarya",
    age=22,
    course="Python",
    city="Trivandrum"
)

"""
output
name: Aiswarya
age: 22
course: Python
city: Trivandrum
"""