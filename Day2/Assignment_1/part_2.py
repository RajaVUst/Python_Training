num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print()
print(f"{'Operation':<12}{'Op':^5}{'Result':>10}")
print("-" * 27)

print(f"{'Addition':<12}{'+':^5}{num1 + num2:>10.2f}")
print(f"{'Subtraction':<12}{'-':^5}{num1 - num2:>10.2f}")
print(f"{'Multiplication':<12}{'*':^5}{num1 * num2:>10.2f}")
print(f"{'Division':<12}{'/':^5}{num1 / num2:>10.2f}")
print(f"{'Floor Division':<12}{'//':^5}{num1 // num2:>10.2f}")
print(f"{'Modulo':<12}{'%':^5}{num1 % num2:>10.2f}")
print(f"{'Power':<12}{'**':^5}{num1 ** num2:>10.2f}")