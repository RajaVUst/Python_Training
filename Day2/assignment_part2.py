 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
remainder = num1 % num2
exponent = num1 ** num2
 
print(f"{'Operation':<12}{'Operator':^5}{'Result':>10}")
print("-" * 27)
print(f"{'Addition':<12}{'+':^5}{addition:>10.2f}")
print(f"{'Subtraction':<12}{'-':^5}{subtraction:>10.2f}")
print(f"{'Multiplication':<12}{'*':^5}{multiplication:>10.2f}")
print(f"{'Division':<12}{'/':^5}{division:>10.2f}")
print(f"{'Floor Division':<12}{'//':^5}{floor_division:>10.2f}")
print(f"{'Modulus':<12}{'%':^5}{remainder:>10.2f}")
print(f"{'Exponent':<12}{'**':^5}{exponent:>10.2f}")