def is_palindrome(word):
    cleaned = word.lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("level"))   # True
print(is_palindrome("python"))  # False
print(is_palindrome("Madam"))   # True  (case-insensitive)
