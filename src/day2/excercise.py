s = input("Enter a sentence: ")

clean_sen = s.replace(" ", "").lower()
reversed_sent = s[::-1]
words = s.split()

first_word = words[0]
last_word = words[-1]

is_palindrome = (clean_sentence == clean_sentence[::-1])

print(f"Length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Reversed: {reversed_sentence}")
print(f"Word count: {len(words)}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Palindrome: {is_palindrome}")

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print()
print(f"{'Operation':<22}{'Op':^3}{'Result':>9}")
print("-" * 34)

print(f"{'Addition':<22}{'+':^3}{n1 + n2:>9.2f}")
print(f"{'Subtraction':<22}{'-':^3}{n1 - n2:>9.2f}")
print(f"{'Multiplication':<22}{'*':^3}{n1 * n2:>9.2f}")
print(f"{'Division':<22}{'/':^3}{n1 / n2:>9.2f}")
print(f"{'Floor Division':<22}{'//':^3}{n1 // n2:>9.2f}")
print(f"{'Modulo':<22}{'%':^3}{n1 % n2:>9.2f}")
print(f"{'Power':<22}{'**':^3}{n1 ** n2:>9.2f}")
