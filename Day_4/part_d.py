#task 11
def multiply(a,b):
    '''Multiplication of two numbers'''
    return a * b

def is_even_print(n):
    '''To find if the number is even or odd'''
    if n % 2 == 0:
        print("It is even number")
    else :
        print("It is odd number")  

help(multiply)
help(is_even_print)

#output
'''Help on function multiply in module __main__:                                                 

multiply(a, b)
    Multiplication of two numbers

Help on function is_even_print in module __main__:                                            

is_even_print(n)
    To find if the number is even or odd'''

#task 12

def reset_score():
    score = 0
reset_score()
#print(score)

#output
''' print(score)
NameError: name 'score' is not defined'''

#task 13

total_attempts = 0
def log_attempt():
    global total_attempts
    total_attempts += 1
log_attempt()
print(total_attempts)
log_attempt()
print(total_attempts)
log_attempt()
print(total_attempts)

#output
'''1
2
3'''

#task 14

def cube(number):
    return(number * number * number)

cube_lambda = lambda num : num * num * num     
print(cube(3))
print(cube_lambda(3))

#output
'''27
27'''

#task 15

def countdown(n):
    print(n)
    if n == 0:
        return 0
    return countdown(n -1)
countdown(5)

#output
'''5
4
3
2
1
0'''

#task 16
def sum_upto(n):
    if n == 1:
        return 1
    return n + sum_upto(n - 1)
print(sum_upto(5))

#output 
'''15'''