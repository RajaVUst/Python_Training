word=input("enter the word:")
reverse=word[::-1]
if(word==reverse):
    print(f"The word is palindrome :{word}")
else:
    print(f"The word is not  palindrome:{word}")


#Without using if else

word1=input("enter the word:")
is_palindrome=word1==word1[::-1]
print(is_palindrome)