#------Multiply--------

def multiply(a, b):
    return a * b

a = int(input("enter the 1st number:"))
b = int(input("enter the second number:"))
result = multiply(a, b)
print(f"The result of both number is:{result}")

# Output:
# enter the 1st number:5
# enter the second number:4
# The result of both number is:20


# Function that prints the result
def is_even_print(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Function that returns the result
def is_even_return(n):
    return n % 2 == 0

# Call both functions with 7
is_even_print(7)
result = is_even_return(7)
print(result)

# Output:
# Odd
# False

def celsius_to_fahrenheit(celsius):
    F = celsius * 9/5 + 32
    return F

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))

# Output:
# 32.0
# 98.6
# 212.0
