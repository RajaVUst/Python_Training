# Task 4
def multiply(a,b):
    return a*b;

result = multiply(50,4)
print(result)       # Output 200 

# Task 5
def is_even_print(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def is_even_return(n):
    if n%2 == 0:
        return True
    else:
        return False
                            # Output
is_even_print(7)            # Odd
print(is_even_return(7))    # False

# Task 6
def celsius_to_fahrenheit(celsius):
    return (celsius*9)/5 +32;
                                                                        # Output
print(f"celsius_to_fahrenheit(0) -> {celsius_to_fahrenheit(0)}")        # celsius_to_fahrenheit(0) -> 32.0
print(f"celsius_to_fahrenheit(37) -> {celsius_to_fahrenheit(37)}")      # celsius_to_fahrenheit(37) -> 98.6
print(f"celsius_to_fahrenheit(100) -> {celsius_to_fahrenheit(100)}")    # celsius_to_fahrenheit(100) -> 212.0
