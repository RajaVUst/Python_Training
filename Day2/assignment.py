# Part 1 - String Manipulation Script
sentence = input("Enter something: ")
print(f"Length {len(sentence)}")
print(f"{sentence.upper()} \n{sentence.lower()}")
print(f"{sentence[::-1]}")

words = sentence.split()
print(f"Word count {len(words)}")
print(f"{words[0]} and {words[-1]}")

clean = sentence.strip().lower()
print(f"Is Palindrome {clean==clean[::-1]}")

# Part 2 - Simple Calculator, Revisited
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{'Label':<12}{'operator':^5}{'result':>10}")
print(f"{'Addition':<12}{'+':^5}{num1+num2:>10.2f}")
print(f"{'Subtraction':<12}{'-':^5}{num1-num2:>10.2f}")
print(f"{'Production':<12}{'*':^5}{num1*num2:>10.2f}")
print(f"{'Division':<12}{'/':^5}{num1/num2:>10.2f}")
print(f"{'Quotient':<12}{'//':^5}{num1//num2:>10.2f}")
print(f"{'Remainder':<12}{'%':^5}{num1%num2:>10.2f}")
print(f"{'Power':<12}{'**':^5}{num1**num2:>10.2f}")