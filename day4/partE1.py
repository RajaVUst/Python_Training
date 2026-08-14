def is_palindrome(word):
    if word.lower()==word[::-1].lower():
        return True
    else:
        return False

word=input("Enter the word to be checked:")

print(f"the given word is palindrome:{is_palindrome(word)}")

# OUTPUT
# Enter the word to be checked:level
# the given word is palindrome:True

# Enter the word to be checked:python
# the given word is palindrome:False

# Enter the word to be checked:Madam
# the given word is palindrome:True

