# Task 11
def multiply(a,b):
    """ Returns the product of given two numbers """
    return a*b;

def is_even_print(n):
    """ Checks whether given number is even or odd"""
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

help(multiply)  # Help on function multiply in module __main__:      
                # multiply(a, b)
                #     Returns the product of given two numbers

help(is_even_print) # Help on function is_even_print in module __main__: 
                    # is_even_print(n)
                    #     Checks whether given number is even or odd

# Task 12
def reset_score():
    score = 0

print(score)    # NameError: score is not defined error because score is local to function

# Task 13
total_attempts = 0
def log_attempt():
    global total_attempts
    total_attempts += 1

log_attempt()
print(total_attempts)   # 1
log_attempt()
print(total_attempts)   # 2
log_attempt()
print(total_attempts)   # 3

# Task 14
cube = lambda x: x**3
print(cube(3))          # 27

def cubes(x):
    return x**3
print(cubes(3))         # 27

# Task 15
def countdown(n):
    if n == 0:
        print("Liftoff!")
    else:
        print(n,end = ' ')
        countdown(n-1)

countdown(15)       # 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 Liftoff!

# Task 16
def sum_upto(n):
    if n == 1: return 1
    return n + sum_upto(n-1)

print(sum_upto(5))  # 15
print(sum_upto(1))  # 1