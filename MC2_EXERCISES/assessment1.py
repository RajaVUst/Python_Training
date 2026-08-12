# String Manipulation

sentence = input("Enter sentence: ")

print(f"Total Length: {len(sentence)}")
print(f"Upper and Lower Case: {sentence.upper() ,sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")
print(f"Word count: {len(sentence.split())}")
print(f"First Word and Last Word: {sentence.split()[0], sentence.split()[-1]}")
print(f"is palindrome: {sentence.lower().replace(" ", "")[::-1]==sentence.lower().replace(" ", "")}")

# Simple Calculator

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

sum = num1+num2
diff = num1-num2
mult = num1*num2
div = num1/num2
mod = num1%num2
floor = num1//num2
exp = num1**num2

print(f"{'Operation':<15}{'Operator':^5}{'Result':>13}")
print(f"{'Addition':<15}{'+':^5}{sum:>15.2f}")
print(f"{'Subtraction':<15}{'-':^5}{diff:>15.2f}")
print(f"{'Multiplication':<15}{'*':^5}{mult:>15.2f}")
print(f"{'Division':<15}{'/':^5}{div:>15.2f}")
print(f"{'Modulus':<15}{'%':^5}{mod:>15.2f}")
print(f"{'Floor':<15}{'//':^5}{floor:>15.2f}")
print(f"{'Exponential':<15}{'**':^5}{exp:>15.2f}")



