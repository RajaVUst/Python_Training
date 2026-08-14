# Task 4
def product(a, b):
    return a * b
result = product(3, 4)
print(result)

#output
# 12

# Task 5

def is_even_print(n):
    if n % 2 == 0:
        print(f'{n} is Even')
    else:
        print(f'Odd')
def  is_even_return(n):
     if n % 2 == 0:
        return True
     else:
        return False
n1 = is_even_print(7)
n2 = is_even_return(7)
print(n2)

# output
# odd
# false

#Task 6

def  celsius_to_fahrenheit(c):
     return c * 9/5 + 32
a = print(celsius_to_fahrenheit(0))
b = print(celsius_to_fahrenheit(100))
c = print(celsius_to_fahrenheit(37))