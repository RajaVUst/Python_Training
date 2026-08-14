# Function definition

def say_hello():
    print( "Hello, Python learner!")

say_hello()
say_hello()
say_hello()

"""
Output ->
Hello, Python learner!
Hello, Python learner!
Hello, Python learner!
"""

# Parameterized funcion

def greet_user(name):
    print(f"Welcome {name}!!!")

greet_user("pranav")
greet_user("paru")

"""
OUtput ->
Welcome pranav!!!
Welcome paru!!!
"""

# Square of a number

def square_of_number(number):
    print(number**2)

square_of_number(5)
square_of_number(2)
square_of_number(-2)

"""
Output ->
25
4
4
"""