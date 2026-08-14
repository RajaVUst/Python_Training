def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print_student_info(
    name="Aakash",
    age=22,
    course="Computer Science",
    city="Chennai"
)