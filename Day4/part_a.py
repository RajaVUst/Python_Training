# Part A: Defining and Calling Functions

# Task 1
def say_hello():
    print("Hello, Python learner!")
say_hello()
say_hello()
say_hello()
# Output:
# Hello, Python learner!
# Hello, Python learner!
# Hello, Python learner!


# Task 2
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")
greet_user("Varsha")
greet_user("vani")
# Output:
# Hello, Varsha! Welcome to Python.
# Hello, vani! Welcome to Python.


# Task 3
def show_square(number):
    print(f"Square of {number} = {number ** 2}")
show_square(5)
show_square(-4)
show_square(10)
# Output:
# Square of 5 = 25
# Square of -4 = 16
# Square of 10 = 100