# **kwargs

def print_student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

print_student_info(
    name="Logesh",
    age=22,
    course="Python",
    city="Chennai")

# Output:
# name : Logesh
# age : 22
# course : Python
# city : Chennai