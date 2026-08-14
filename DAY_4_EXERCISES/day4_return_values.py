# Multiply 2 numbers 

def multiply(a,b):
    return a*b

result = multiply(5,2)
print(result)

# 10

# Odd or Even Result printing

def odd_or_even_print(number):
    if number%2==0:
        print("Even")
    else:
        print("Odd")

odd_or_even_print(7)

# Odd

# Odd or Even Result return

def odd_or_even_return_result(number):
    if number%2==0:
        return True
    else:
        return False

print(odd_or_even_return_result(7))

# False

# Celcius to Faherenheit

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print("0°C =", celsius_to_fahrenheit(0), "°F")
print("37°C =", celsius_to_fahrenheit(37), "°F")
print("100°C =", celsius_to_fahrenheit(100), "°F")

"""
Output -> 
0°C = 32.0 °F
37°C = 98.6 °F
100°C = 212.0 °F
"""