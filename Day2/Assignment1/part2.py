# Part 2 - Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
power = num1 ** num2

print("\n----- Calculator Results -----")
print(f"{'Operation':<12}{'Op':^5}{'Result':>10}")
print("-" * 27)
print(f"{'Addition':<12}{'+':^5}{addition:>10.2f}")
print(f"{'Subtract':<12}{'-':^5}{subtraction:>10.2f}")
print(f"{'Multiply':<12}{'*':^5}{multiplication:>10.2f}")
print(f"{'Divide':<12}{'/':^5}{division:>10.2f}")
print(f"{'Floor Div':<12}{'//':^5}{floor_division:>10.2f}")
print(f"{'Modulo':<12}{'%':^5}{modulus:>10.2f}")
print(f"{'Power':<12}{'**':^5}{power:>10.2f}")