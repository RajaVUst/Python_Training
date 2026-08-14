# Palindrome

def is_palindrome(word):
    word = word.lower()

    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome("level"))
print(is_palindrome("python"))
print(is_palindrome("Madam"))

# Output:
# True
# False
# True