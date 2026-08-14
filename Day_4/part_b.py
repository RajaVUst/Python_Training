#task 4
def multiply(a,b):
    return a * b
a = 89
b = 2
c = multiply(a,b)
print(c)

#output
'''178'''

#task 5
def is_even_print(n):
    if n % 2 == 0:
        print("It is even number")
    else :
        print("It is odd number")  

def is_even_return(n):
    return n % 2 == 0
n = 7
is_even_print(n)
print(is_even_return(n))

#output
'''It is odd number
False'''

#task 6
def celsius_to_fahrenheit(C):
    return C * 9/5 + 32
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))

#output
'''32.0
98.6
212.0'''