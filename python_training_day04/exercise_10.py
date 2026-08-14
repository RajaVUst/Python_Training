def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(
    name="Deepa",
    age=21,
    course="ECE",
    city="Coimbatore"
)


#output:
'''name: Deepa
age: 21
course: ECE
city: Coimbatore'''