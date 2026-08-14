# Q1
def say_hello():
    print("Hello, Python learner!")

say_hello()
say_hello()
say_hello()

# Q2
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Shoaib")
greet_user("Ejaz")

# Q3
def show_square(number):
    print(number ** 2)

show_square(5)
show_square(-4)
show_square(10)

# Q4
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)

# Q5
def is_even_print(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def is_even_return(n):
    return n % 2 == 0

is_even_print(7)
print(is_even_return(7))

# Q6
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))

# Q7
def order_summary(item, quantity=1):
    print(f"Item: {item}, Quantity: {quantity}")

order_summary("Laptop")
order_summary("Mouse", 3)

# Q8
def book_ticket(passenger, seat_type="Economy", meal="Veg"):
    print(f"Passenger: {passenger}, Seat: {seat_type}, Meal: {meal}")

book_ticket("Reni")
book_ticket("Reni", meal="Non-Veg")
book_ticket("Reni", meal="Veg", seat_type="Business")

# Q9
def total_cost(*prices):
    return sum(prices)

print(total_cost(100, 200))
print(total_cost(100, 200, 300, 400, 500))

# Q10
def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(
    name="Shoaib",
    age=24,
    course="Python",
    city="Trivandrum"
)

# Q11
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

print(multiply.__doc__)
print(celsius_to_fahrenheit.__doc__)

# Q12
def reset_score():
    score = 0
    print(score)

reset_score()


# Q13
total_attempts = 0

def log_attempt():
    global total_attempts
    total_attempts += 1

log_attempt()
log_attempt()
log_attempt()

print(total_attempts)

# Q14
cube = lambda n: n ** 3

print(cube(3))

def cube_function(n):
    return n ** 3

print(cube_function(3))

# Q15
def countdown(n):
    if n == 0:
        print("Liftoff!")
        return

    print(n)
    countdown(n - 1)

countdown(5)

# Q16

def sum_upto(n):
    if n == 1:
        return 1

    return n + sum_upto(n - 1)

print(sum_upto(5))

# Q17
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("level"))
print(is_palindrome("python"))
print(is_palindrome("Madam"))

# Q18
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
    print(f"{score} -> {grade_from_score(score)}")

# Q19
def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("Python Bootcamp"))
print(count_vowels("Functions are useful"))

# Q20
def fizzbuzz_range(start, end):
    for num in range(start, end + 1):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz_range(1, 20)

# Q21
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def primes_up_to(limit):
    primes = []

    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)

    return primes

print(primes_up_to(30))

# Q22
def password_strength(password):
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)

    if len(password) >= 8 and has_digit and has_upper:
        return "Strong"
    elif len(password) >= 6:
        return "Medium"
    else:
        return "Weak"

print(password_strength("abc"))
print(password_strength("python12"))
print(password_strength("Python123"))

# Q23
def build_utilities(operation, *values):
    if operation == "sum":
        return sum(values)
    elif operation == "max":
        return max(values)
    elif operation == "min":
        return min(values)
    elif operation == "average":
        return sum(values) / len(values)

print(build_utilities("sum", 4, 8, 15))
print(build_utilities("average", 2, 4, 6, 8))