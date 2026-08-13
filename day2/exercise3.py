word=input("enter the word to be checked as palindrome")

is_palindrome=(word==word[::-1])
print(is_palindrome)