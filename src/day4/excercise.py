# PART A
def say_hello():
    print("Hello, Python learner!")


say_hello() # prints hello , python learner!
say_hello() # prints hello , python learner!
say_hello() # prints hello , python learner!

# Task 2
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

name1 = input("Enter your name: ")
name2 = input("Enter your classmate's name: ")

greet_user(name1) #prints Hello, Bijo! Welcome to Python
greet_user(name2) #prints Hello, Zack! Welcome to Python

# Task 3
def show_square(number):
    print(f"The square of {number} is {number * number}")

show_square(5) #prints The square of 5 is 25
show_square(10) #prints The square of 10 is 100
show_square(-4) #prints The square of -4 is 16

# PART B
def multiply(a, b):
    return a * b


result = multiply(5, 4)
print("Task 4 result:", result) #prints 20

# Task 5

def is_even_print(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


def is_even_return(n):
    if n % 2 == 0:
        return True
    else:
        return False


is_even_print(7)

result = is_even_return(7)
print("Is 7 even?", result)

# Task 6
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


print("0 Celsius =", celsius_to_fahrenheit(0))
print("37 Celsius =", celsius_to_fahrenheit(37))
print("100 Celsius =", celsius_to_fahrenheit(100))

# part C
def order_summary(item, quantity=1):
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")

order_summary("Laptop")
order_summary("Notebook", 5)

# Task 8
def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}")
    print(f"Seat Type: {seat_type}")
    print(f"Meal: {meal}")
    print()

book_ticket("Joel")

book_ticket("John", meal="Non-Veg")

book_ticket("David", meal="Non-Veg", seat_type="Business")


 
# Task 9
def total_cost(*prices):
    total = 0

    for price in prices:
        total = total + price

    return total


print("Total of 2 prices:", total_cost(100, 200))

print("Total of 5 prices:", total_cost(100, 200, 300, 400, 500))

# Task 10
def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print_student_info(
    name="Joel",
    age=23,
    course="Python",
    city="Chennai"
)


# PART D

# Task 11

def multiply_with_docstring(a, b):
    """Returns the product of two numbers."""
    return a * b


def celsius_to_fahrenheit_with_docstring(celsius):
    """Converts Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


print(multiply_with_docstring(5, 3))
print(celsius_to_fahrenheit_with_docstring(100))
 
# Task 12
def reset_score():
    score = 0
    print("Score inside function:", score)


reset_score()


# Task 13
total_attempts = 0


def log_attempt():
    global total_attempts
    total_attempts = total_attempts + 1


log_attempt()
log_attempt()
log_attempt()

print("Total attempts:", total_attempts)


 
# Task 14
cube = lambda number: number * number * number

print("Cube using lambda:", cube(3))


def cube_regular(number):
    return number * number * number


print("Cube using regular function:", cube_regular(3))


 
# Task 15
def countdown(n):

    if n == 0:
        print("Liftoff!")
    else:
        print(n)
        countdown(n - 1)


countdown(5)


 
# Task 16

def sum_upto(n):

    if n == 1:
        return 1
    else:
        return n + sum_upto(n - 1)


print("sum_upto(5):", sum_upto(5))
print("sum_upto(1):", sum_upto(1))

# PART E: 
# Task 17
def is_palindrome(word):
    word = word.lower()

    if word == word[::-1]:
        return True
    else:
        return False


print("level:", is_palindrome("level"))
print("python:", is_palindrome("python"))
print("Madam:", is_palindrome("Madam"))


 
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
    print(f"{score} -> {grade}")


 
# Task 19
def count_vowels(text):
    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count = count + 1

    return count


print("Vowels in Python Bootcamp:", count_vowels("Python Bootcamp"))
print("Vowels in Hello, how are you?:", count_vowels("Hello, how are you?"))


 
# Task 20
def fizzbuzz_range(start, end):

    for number in range(start, end + 1):

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")

        elif number % 3 == 0:
            print("Fizz")

        elif number % 5 == 0:
            print("Buzz")

        else:
            print(number)


fizzbuzz_range(1, 20)


 
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


print("Prime numbers up to 30:")
print(primes_up_to(30))


 
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


print("Password 1:", password_strength("hello"))
print("Password 2:", password_strength("hello12"))
print("Password 3:", password_strength("Hello123"))


 
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


print(build_utilities("sum", 4, 8, 15))
print(build_utilities("average", 2, 4, 6, 8))

