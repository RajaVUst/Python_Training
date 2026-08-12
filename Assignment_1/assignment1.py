##PART 1######
sentence = "This is pavan I'm hyderabad"
length = len(sentence)
upper = sentence.upper()
lower = sentence.lower()
reverse = sentence[::-1]
word_count = len(sentence.split())
words = sentence.split()
first_word = words[0]
last_word = words[-1]
palindrome = sentence.replace(' ','').lower()
palindrome = palindrome[::-1]
if palindrome == sentence:
    print("sentence is palindrome")
else:
    print("it is not palindrome")
print(f"length of the sentence : {length}")
print(f"upper of the sentence : {upper}")
print(f"lower of the sentence : {lower}")
print(f"reverse of the sentence : {reverse}")
print(f"word_count of the sentence :{word_count}")
print(f"first word of the sentence : {first_word}")
print(f"last word of the sentence : {last_word}")
#####PART 2####
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{'Operation':<12}{'Op':^5}{'Result':>12}")
print("-" * 29)

print(f"{'Addition':<12}{'+':^5}{num1 + num2:>12.2f}")
print(f"{'Subtraction':<12}{'-':^5}{num1 - num2:>12.2f}")
print(f"{'Multiplication':<12}{'*':^5}{num1 * num2:>12.2f}")
print(f"{'Division':<12}{'/':^5}{num1 / num2:>12.2f}")
print(f"{'Floor Division':<12}{'//':^5}{num1 // num2:>12.2f}")
print(f"{'Modulus':<12}{'%':^5}{num1 % num2:>12.2f}")
print(f"{'Power':<12}{'**':^5}{num1 ** num2:>12.2f}")