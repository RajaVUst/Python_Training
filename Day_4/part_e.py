#task 17
def is_palindrome(word):
    if(word == word[::-1]):
        print(f"The word {word} is palindrome")
    else:
        print(f"The word {word} is not palindrome")

is_palindrome("level")
is_palindrome("Madam")
is_palindrome("python")

#task 18
def grade_from_score(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

scores = [95, 82, 61, 40, 100]

for score in scores:
    print(f"{score} -> {grade_from_score(score)}")


#task 19

def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("Python Bootcamp"))
print(count_vowels("Learning Python is fun"))

#task 20

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


#task 21

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

#task 22

def password_strength(password):
    has_upper = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True

    if len(password) >= 8 and has_upper and has_digit:
        return "Strong"
    elif len(password) >= 6:
        return "Medium"
    else:
        return "Weak"


print(password_strength("abc"))
print(password_strength("python1"))
print(password_strength("Python123"))

#task 23

def build_utilities(operation, *values):

    if operation == "sum":
        return sum(values)

    elif operation == "max":
        return max(values)

    elif operation == "min":
        return min(values)

    elif operation == "average":
        return sum(values) / len(values)

    else:
        return "Invalid operation"


print(build_utilities("sum", 4, 8, 15))
print(build_utilities("average", 2, 4, 6, 8))
print(build_utilities("max", 10, 5, 20, 7))
print(build_utilities("in", 10, 5, 20, 7))