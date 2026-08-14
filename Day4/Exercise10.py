def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
 
print_student_info(name="Sara", age=21, course="Python", city="Chennai")

# Output:
# name: Sara
# age: 21
# course: Python
# city: Chennai