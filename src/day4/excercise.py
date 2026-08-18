# PART A
def say_hello():
    print("Hello, Python learner!")  #prints Hello, Python learner!


say_hello() # prints hello , python learner!
say_hello() # prints hello , python learner!
say_hello() # prints hello , python learner!

# Task 2
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")  #prints Hello, Bijo! Welcome to Python


name1 = input("Enter your name: ")
name2 = input("Enter your classmate's name: ")

greet_user(name1) #prints Hello, Bijo! Welcome to Python
greet_user(name2) #prints Hello, Zack! Welcome to Python

# Task 3
def show_square(number):
    print(f"The square of {number} is {number * number}")  #prints The square of 5 is 25


show_square(5) #prints The square of 5 is 25
show_square(10) #prints The square of 10 is 100
show_square(-4) #prints The square of -4 is 16


# PART B
def multiply(a, b):
    return a * b


result = multiply(5, 4)
print("Task 4 result:", result) #prints Task 4 result: 20


# Task 5
def is_even_print(n):
    if n % 2 == 0:
        print("Even")  #prints Even
    else:
        print("Odd")  #prints Odd


def is_even_return(n):
    if n % 2 == 0:
        return True
    else:
        return False


is_even_print(7)  #prints Odd

result = is_even_return(7)
print("Is 7 even?", result)  #prints Is 7 even? False


# Task 6
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


print("0 Celsius =", celsius_to_fahrenheit(0))  #prints 0 Celsius = 32.0
print("37 Celsius =", celsius_to_fahrenheit(37))  #prints 37 Celsius = 98.6
print("100 Celsius =", celsius_to_fahrenheit(100))  #prints 100 Celsius = 212.0


# PART C
def order_summary(item, quantity=1):
    print(f"Item: {item}")  #prints Item: Laptop
    print(f"Quantity: {quantity}")  #prints Quantity: 1


order_summary("Laptop")
order_summary("Notebook", 5)


# Task 8
def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}")  #prints Passenger: Joel
    print(f"Seat Type: {seat_type}")  #prints Seat Type: Economy
    print(f"Meal: {meal}")  #prints Meal: Veg
    print()  #prints a blank line


book_ticket("Joel")

book_ticket("John", meal="Non-Veg")

book_ticket("David", meal="Non-Veg", seat_type="Business")


# Task 9
def total_cost(*prices):
    total = 0

    for price in prices:
        total = total + price

    return total


print("Total of 2 prices:", total_cost(100, 200))  #prints Total of 2 prices: 300
print("Total of 5 prices:", total_cost(100, 200, 300, 400, 500))  #prints Total of 5 prices: 1500


# Task 10
def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")  #prints each student's detail


print_student_info(
    name="Joel",
    age=23,
    course="Python",
    city="Chennai"
)
#prints name: Joel
#prints age: 23
#prints course: Python
#prints city: Chennai


# PART D

# Task 11
def multiply_with_docstring(a, b):
    """Returns the product of two numbers."""
    return a * b


def celsius_to_fahrenheit_with_docstring(celsius):
    """Converts Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


print(multiply_with_docstring(5, 3))  #prints 15
print(celsius_to_fahrenheit_with_docstring(100))  #prints 212.0


# Task 12
def reset_score():
    score = 0
    print("Score inside function:", score)  #prints Score inside function: 0


reset_score()


# Task 13
total_attempts = 0


def log_attempt():
    global total_attempts
    total_attempts = total_attempts + 1


log_attempt()
log_attempt()
log_attempt()

print("Total attempts:", total_attempts)  #prints Total attempts: 3


# Task 14
cube = lambda number: number * number * number

print("Cube using lambda:", cube(3))  #prints Cube using lambda: 27


def cube_regular(number):
    return number * number * number


print("Cube using regular function:", cube_regular(3))  #prints Cube using regular function: 27


# Task 15
def countdown(n):

    if n == 0:
        print("Liftoff!")  #prints Liftoff!
    else:
        print(n)  #prints the current countdown number
        countdown(n - 1)


countdown(5)
#prints 5
#prints 4
#prints 3
#prints 2
#prints 1
#prints Liftoff!


# Task 16
def sum_upto(n):

    if n == 1:
        return 1
    else:
        return n + sum_upto(n - 1)


print("sum_upto(5):", sum_upto(5))  #prints sum_upto(5): 15
print("sum_upto(1):", sum_upto(1))  #prints sum_upto(1): 1


# PART E

# Task 17
def is_palindrome(word):
    word = word.lower()

    if word == word[::-1]:
        return True
    else:
        return False


print("level:", is_palindrome("level"))  #prints level: True
print("python:", is_palindrome("python"))  #prints python: False
print("Madam:", is_palindrome("Madam"))  #prints Madam: True


# Task 18
def grade_from_score(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


scores = [95, 82, 61, 40, 100]

for score in scores:
    grade = grade_from_score(score)
    print(f"{score} -> {grade}")  #prints the score and its grade

#prints 95 -> A
#prints 82 -> B
#prints 61 -> D
#prints 40 -> F
#prints 100 -> A


# Task 19
def count_vowels(text):
    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count = count + 1

    return count


print("Vowels in Python Bootcamp:", count_vowels("Python Bootcamp"))  #prints Vowels in Python Bootcamp: 4
print("Vowels in Hello, how are you?:", count_vowels("Hello, how are you?"))  #prints Vowels in Hello, how are you?: 8


# Task 20
def fizzbuzz_range(start, end):

    for number in range(start, end + 1):

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")  #prints FizzBuzz

        elif number % 3 == 0:
            print("Fizz")  #prints Fizz

        elif number % 5 == 0:
            print("Buzz")  #prints Buzz

        else:
            print(number)  #prints the current number


fizzbuzz_range(1, 20)

#prints 1
#prints 2
#prints Fizz
#prints 4
#prints Buzz
#prints Fizz
#prints 7
#prints 8
#prints Fizz
#prints Buzz
#prints 11
#prints Fizz
#prints 13
#prints 14
#prints FizzBuzz
#prints 16
#prints 17
#prints Fizz
#prints 19
#prints Buzz


# Task 21
def is_prime(n):

    if n < 2:
        return False

    for number in range(2, n):

        if n % number == 0:
            return False

    return True


def primes_up_to(limit):

    primes = []

    for number in range(2, limit + 1):

        if is_prime(number):
            primes.append(number)

    return primes


print("Prime numbers up to 30:")  #prints Prime numbers up to 30:
print(primes_up_to(30))  #prints [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# Task 22
def password_strength(password):

    has_digit = False
    has_uppercase = False

    for character in password:

        if character.isdigit():
            has_digit = True

        if character.isupper():
            has_uppercase = True

    if len(password) >= 8 and has_digit and has_uppercase:
        return "Strong"

    elif len(password) >= 6 and (has_digit or has_uppercase):
        return "Medium"

    else:
        return "Weak"


print("Password 1:", password_strength("hello"))  #prints Password 1: Weak
print("Password 2:", password_strength("hello12"))  #prints Password 2: Medium
print("Password 3:", password_strength("Hello123"))  #prints Password 3: Strong


# Task 23
def build_utilities(operation, *values):

    if operation == "sum":

        total = 0

        for value in values:
            total = total + value

        return total

    elif operation == "max":

        largest = values[0]

        for value in values:
            if value > largest:
                largest = value

        return largest

    elif operation == "min":

        smallest = values[0]

        for value in values:
            if value < smallest:
                smallest = value

        return smallest

    elif operation == "average":

        total = 0

        for value in values:
            total = total + value

        return total / len(values)

    else:
        return "Invalid operation"


print(build_utilities("sum", 4, 8, 15))  #prints 27
print(build_utilities("average", 2, 4, 6, 8))  #prints 5.0
