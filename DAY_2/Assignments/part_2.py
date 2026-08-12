num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
mod = num1 % num2
power = num1 ** num2

print(f"{'Addition':<15}{'+':^5}{sum:>10.2f}")
print(f"{'Subtraction':<15}{'-':^5}{sub:>10.2f}")
print(f"{'Multiplication':<15}{'*':^5}{mul:>10.2f}")
print(f"{'Division':<15}{'/':^5}{div:>10.2f}")
print(f"{'Floor Division':<15}{'//':^5}{floor_div:>10.2f}")
print(f"{'Modulus':<15}{'%':^5}{mod:>10.2f}")
print(f"{'Power':<15}{'**':^5}{power:>10.2f}")