num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
 
try:
    result = (num1) / (num2)
    print("Result:", result)
 
except ValueError:
    print("Invalid number entered.")
 
except ZeroDivisionError:
    print("Cannot divide by zero.")
 
# Output:
# Enter first number: 10
# Enter second number: 0
# Cannot divide by zero.
 
# Output:
# Enter first number: 10
# Enter second number: 2
# Result: 5.0
 