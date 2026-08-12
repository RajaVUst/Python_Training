#Simple Calculator, Revisited
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{'Operation':<12}{'Operator':^10}{'Result':>12}")
print("-" * 34)

print(f"{'Addition':<12}{'+':^10}{num1 + num2:>12.2f}")
print(f"{'Subtraction':<12}{'-':^10}{num1 - num2:>12.2f}")
print(f"{'Multiplication':<12}{'*':^10}{num1 * num2:>12.2f}")
print(f"{'Division':<12}{'/':^10}{num1 / num2:>12.2f}")
print(f"{'Floor Division':<12}{'//':^10}{num1 // num2:>12.2f}")
print(f"{'Modulus':<12}{'%':^10}{num1 % num2:>12.2f}")
print(f"{'Power':<12}{'**':^10}{num1 ** num2:>12.2f}")