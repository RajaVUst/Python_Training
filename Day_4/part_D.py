#Task 11

def product(a, b):
    """Gives the product of a and b """
    return a * b
result = product(3, 4)
print(result)
help(product)
print(product.__doc__)

# Output 

# Help on function product in module __main__:                                                     

# product(a, b)
#     Gives the product of a and b


def  celsius_to_fahrenheit(c):
     """Convert celcius to Fahrenheit"""
     return c * 9/5 + 32
a = print(celsius_to_fahrenheit(0))
help(product)
print(celsius_to_fahrenheit.__doc__)

# Output 

# Help on function product in module __main__:                                                      

# product(a, b)
#     Gives the product of a and b

# Convert celcius to Fahrenheit

# Task 12

def  reset_score():
     score = 0
     print(f'score {score}')
reset_score()
# print(score)

# output 

# module>
#     print(score)
#           ^^^^^
# NameError: name 'score' is not defined

# the error occur here because score is a local variable.
# local variable only exist inside the function which they are created.

# Task 13

total_attempts = 0
def log_attempt():
     global total_attempts
     total_attempts += 1
log_attempt()
log_attempt()
log_attempt()
print(f'Total attempts: {total_attempts}')

# Output 

# Total attempts: 3


# Task 15

def countdown(n):
     if n == 0:
      print('lift off')
     else:
        print(n)
        countdown(n - 1)
countdown(5)   

#Out put

# 5
# 4
# 3
# 2
# 1
# lift off

# Task 16

def sum_upto(n):
   if n == 1:  # base case
       return 1
   else:       # recursice case
       return n + sum_upto(n - 1)
print(sum_upto(5))

# Output 

# 15

# Task 17 

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
print(is_palindrome('level'))
print(is_palindrome('python'))
print(is_palindrome('Madam'))

# Output

# True
# False
# True

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
    print(f"{score} -> {grade_from_score(score)}")
