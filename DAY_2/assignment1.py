# Assignment 1 (Graded) - Day 2
# Part 1: String Manipulation Script
# Part 2: Simple Calculator, Revisited

# ============================================================
# PART 1 - String Manipulation Script
# ============================================================

sentence = input("Enter a sentence: ")

words = sentence.split()
cleaned = sentence.replace(" ", "").lower()

print(f"\nTotal length    : {len(sentence)}")
print(f"Uppercase       : {sentence.upper()}")
print(f"Lowercase       : {sentence.lower()}")
print(f"Reversed        : {sentence[::-1]}")
print(f"Word count      : {len(words)}")
print(f"First word      : {words[0]}")
print(f"Last word       : {words[-1]}")
print(f"Is palindrome   : {cleaned == cleaned[::-1]}")

# ============================================================
# PART 2 - Simple Calculator, Revisited
# ============================================================

print("\n")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))

print(f"\n{'Operation':<15}{'Op':^5}{'Result':>10}")
print("-" * 30)
print(f"{'Addition':<15}{'+'  :^5}{num1 + num2        :>10.2f}")
print(f"{'Subtraction':<15}{'-'  :^5}{num1 - num2        :>10.2f}")
print(f"{'Multiplication':<15}{'*'  :^5}{num1 * num2        :>10.2f}")
print(f"{'Division':<15}{'/'  :^5}{num1 / num2        :>10.2f}")
print(f"{'Floor Division':<15}{'//' :^5}{num1 // num2       :>10.2f}")
print(f"{'Modulus':<15}{'%'  :^5}{num1 % num2        :>10.2f}")
print(f"{'Exponent':<15}{'**' :^5}{num1 ** num2       :>10.2f}")
