#Part1- String Manipulation Script
sentence=input("Enter a sentence: ")
print(f"total length of the sentence is: {len(sentence)}")
print(f"uppercase: {sentence.upper()},lowercase: {sentence.lower()}")
print(f"reversed: {sentence[::-1]}")
print(f"word count: {len(sentence.split())}")
print(f"first word: {sentence.split()[0]}, last word: {sentence.split()[-1]}")
is_palindrome=sentence.strip().lower()==sentence.strip().lower()[::-1]
print(f"Is the sentence a palindrome? {is_palindrome}")



#Part2- Simple Calculator, Revisited
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"{'Addition':<15}{'+':^5}{num1 + num2:>10.2f}")
print(f"{'Subtraction':<15}{'-':^5}{num1 - num2:>10.2f}")
print(f"{'Multiplication':<15}{'*':^5}{num1 * num2:>10.2f}")
print(f"{'Division':<15}{'/':^5}{num1 / num2:>10.2f}")
print(f"{'Exponentiation':<15}{'**':^5}{num1 ** num2:>10.2f}")
print(f"{'Floor Division':<15}{'//':^5}{num1 // num2:>10.2f}")
print(f"{'Modulus':<15}{'%':^5}{num1 % num2:>10.2f}")
