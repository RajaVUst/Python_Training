# Part 2 - Simple Calculator
 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
 
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
remainder = num1 % num2
power = num1 ** num2
 
print()
print("=== Calculator ===")
 
print(f"{'Operation':<15}{'Op':^5}{'Result':>12}")
print("-" * 32)
 
print(f"{'Addition':<15}{'+':^5}{addition:>12.2f}")
print(f"{'Subtraction':<15}{'-':^5}{subtraction:>12.2f}")
print(f"{'Multiplication':<15}{'*':^5}{multiplication:>12.2f}")
print(f"{'Division':<15}{'/':^5}{division:>12.2f}")
print(f"{'Floor Division':<15}{'//':^5}{floor_division:>12.2f}")
print(f"{'Modulus':<15}{'%':^5}{remainder:>12.2f}")
print(f"{'Power':<15}{'**':^5}{power:>12.2f}")