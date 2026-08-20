
#  Predict the output 

def add_item(item, basket=[]):
    basket.append(item)
    return basket


print(add_item("apple"))
print(add_item("banana"))

# Output:
# ['apple']
# ['apple', 'banana']

# The default argument basket=[] is created only once when the
# function is defined. It is not recreated every time the
# function is called.
# Therefore, both function calls use the same list.
#


#  fixed 

def add_item(item, basket=None):
    if basket is None:
        basket = []

    basket.append(item)
    return basket


print(add_item("apple"))
print(add_item("banana"))

# Output:
# ['apple']
# ['banana']


#  Another example 

def add_student(student, students):
    students.append(student)


students = ["Alice", "Bob"]

add_student("Carol", students)

print(students)

# Output:
# ['Alice', 'Bob', 'Carol']
#
# Lists are mutable. When the list is passed to the function,
# the function modifies the original list.
#
# If we want to avoid changing the original list, we can pass
# a copy or create a copy inside the function.


def add_student_safely(student, students):
    new_students = students.copy()
    new_students.append(student)
    return new_students


students = ["Alice", "Bob"]

new_students = add_student_safely("Carol", students)

print("Original:", students)
print("New:", new_students)

# Output:
# Original: ['Alice', 'Bob']
# New: ['Alice', 'Bob', 'Carol']