def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("hello"))
print(is_palindrome("python"))
print(is_palindrome("Madam"))

'''
OUTPUT:
False
False
True
'''