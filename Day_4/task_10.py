def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(
    name="Anjali",
    age=21,
    course="Computer Science",
    city="Trivandrum"
)

# output:
# name: Anjali
# age: 21
# course: Computer Science
# city: Trivandrum