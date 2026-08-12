# PART 1
print("====== PART 1 ======")
 
# input a sentence
sentence = input("Enter a sentence: ")
 
# print total length of the sentence
print(f"Total length: {len(sentence)}")
# print both uppercase and lowercase version of the sentence
print(f"Uppercase: {sentence.upper()} | Lowercase: {sentence.lower()}")
# print the sentence in reverse
print(f"Reversed sentence: {sentence[::-1]}")
# print the word count
print(f"Word count: {len(sentence.split())}")
# print the first and last word of the sentence
print(f"First word: {sentence.split()[0]} | Last Word: {sentence.split()[-1]}")
# check whether the sentence is a palindrome or not and print the result
print(f"Is the sentence a palindrome? {sentence.lower().replace(" ","") == sentence[::-1].lower().replace(" ","")}")
 
# PART 2
print("====== PART 2 ======")
 
# input two numbers from the user
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
 
# print table header

print("\nOperation Output Result")
print("-" * 20)
 
# Print results
print(f"{'Addition':<14}{'+':^5}{number1 + number2:>10.2f}")
print(f"{'Subtraction':<14}{'-':^5}{number1 - number2:>10.2f}")
print(f"{'Multiplication':<12}{'*':^5}{number1 * number2:>10.2f}")
print(f"{'Division':<14}{'/':^5}{number1 / number2:>10.2f}")
print(f"{'Floor Division':<12}{'//':^5}{number1 // number2:>10.2f}")
print(f"{'Modulus':<14}{'%':^5}{number1 % number2:>10.2f}")
print(f"{'Power':<14}{'**':^5}{number1 ** number2:>10.2f}")