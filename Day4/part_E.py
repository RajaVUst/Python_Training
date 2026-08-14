# Task 17
def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False

print(is_palindrome("level"))       # True
print(is_palindrome("python"))      # False
print(is_palindrome("Madam"))       # True

# Task 18
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
    print(f"{score} -> {grade_from_score(score)}", end = ', ')
    # Output: 95 -> A, 82 -> B, 61 -> D, 40 -> F, 100 -> A

# Task 19
def count_vowels(text):
    count = 0
    for character in text.lower():
        if character in "aeiou":
            count += 1
    return count

print(count_vowels("Python Bootcamp"))          # 4
print(count_vowels("Good Management Girls"))    # 7

# Task 20
def fizzbuzz_range(start,end):
    for i in range(start, end+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz_range(9,18)    # Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz

# Task 21
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def primes_up_to(limit):
    li = []
    for i in range(2,limit):
        if is_prime(i):
            li.append(i)
    return li

print(primes_up_to(30)) # [2,3,5,7,11,13,17,19,23,29]

# Task 22
def password_strength(password):
    if len(password) < 6:
        return "Weak"
    else:
        digit,upper = False,False
        for i in password:
            if i.isdigit():
                digit = True
            elif i.isupper():
                upper = True
        if digit and upper:
            return "Strong"
        else:
            return "Medium"

print(password_strength("Shabanam@29")) # Strong
print(password_strength("Arsha"))       # Weak
print(password_strength("Reni009"))     # Strong

# Task 23
def build_utilities(operation, *values):
    if operation == "sum":
        return sum(values)
    elif operation == "max":
        return max(values)
    elif operation == "min":
        return min(values)
    elif operation == "average":
        return sum(values)/len(values)

print(build_utilities('sum',4,8,15))        # 27
print(build_utilities('average',2,4,6,8))   # 5.0