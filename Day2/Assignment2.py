#Simple Calculator, Revisited
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
floordiv = num1 // num2
mod = num1 % num2
power = num1 ** num2

print(f"{'Addition':<12}{'+':^5}{add:>10.2f}")
print(f"{'Subtraction':<12}{'-':^5}{sub:>10.2f}")
print(f"{'Multiplication':<12}{'*':^5}{mul:>10.2f}")
print(f"{'Division':<12}{'/':^5}{div:>10.2f}")
print(f"{'Floor Div':<12}{'//':^5}{floordiv:>10.2f}")
print(f"{'Modulus':<12}{'%':^5}{mod:>10.2f}")
print(f"{'Power':<12}{'**':^5}{power:>10.2f}")