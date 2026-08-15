word=input("enter the word:")
def is_palindrome(word):
    word1=word[::-1]
    if word1==word:
        print(f" The word {word} is palindrome")
    else:
        print(f" The word {word} is not palindrome")
    return

is_palindrome(word)


def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
arr = [95, 82, 61, 40, 100]
result = [f"{score} -> {get_grade(score)}" for score in arr]
print(", ".join(result))

#output =95 -> A, 82 -> B, 61 -> D, 40 -> F, 100 -> A


count=0
def count_vowels(word):
    global count
    for i in range(0,len(word)):
        if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
            count+=1
    return count

print(count_vowels("hi"))

#output=1


def fizzbuzz_range(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz_range(1, 15)

# Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz


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

# Output:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
    if len(password) >= 8 and has_upper and has_lower and has_digit:
        return "Strong"
    elif len(password) >= 6 and has_digit and (has_upper or has_lower):
        return "Medium"
    else:
        return "Weak"

print(password_strength("abc"))
print(password_strength("abc123"))
print(password_strength("Abc12345"))

# Output:
# Weak
# Medium
# Strong

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
print(build_utilities("max", 4, 8, 15))
print(build_utilities("min", 4, 8, 15))

# Output:
# 27
# 5.0
# 15
# 4


