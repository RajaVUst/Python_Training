# Assignment 1 - Part 1
# String Manipulation Script
# sentence = input("Enter a sentence: ")
# cleaned_sentence = sentence.replace(" ", "").lower()
# words = sentence.split()
# print("\n--- String Analysis ---")
# print(f"Total Length   : {len(sentence)}")
# print(f"Uppercase      : {sentence.upper()}")
# print(f"Lowercase      : {sentence.lower()}")
# print(f"Reversed       : {sentence[::-1]}")
# print(f"Word Count     : {len(words)}")
# print(f"First Word     : {words[0]}")
# print(f"Last Word      : {words[-1]}")
# print(f"Palindrome     : {cleaned_sentence == cleaned_sentence[::-1]}")

 
# Assignment 1 - Part 2
# Simple Calculator
first_number = float(input("\nEnter the first number: "))
second_number = float(input("Enter the second number: "))
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
remainder = first_number % second_number
power = first_number ** second_number
 
print("\n--- Calculator ---")
print(f"{'Label':<12}{'Op':^5}{'Result':>10}")
print(f"{'Addition':<12}{'+':^5}{addition:>10.2f}")
print(f"{'Subtraction':<12}{'-':^5}{subtraction:>10.2f}")
print(f"{'Multiplication':<12}{'*':^5}{multiplication:>10.2f}")
print(f"{'Division':<12}{'/':^5}{division:>10.2f}")
print(f"{'Floor Division':<12}{'//':^5}{floor_division:>10.2f}")
print(f"{'Modulus':<12}{'%':^5}{remainder:>10.2f}")
print(f"{'Power':<12}{'**':^5}{power:>10.2f}")