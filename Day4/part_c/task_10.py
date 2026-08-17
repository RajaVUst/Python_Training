def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print_student_info(
    name="Selma",
    age=22,
    course="Python",
    city="Trivandrum"
)


# output
# name: Selma
# age: 22
# course: Python
# city: Trivandrum