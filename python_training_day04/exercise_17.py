def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(f"level -> {is_palindrome('level')}")
print(f"python -> {is_palindrome('python')}")
print(f"Madam -> {is_palindrome('Madam')}")


#output:
'''level -> True
python -> False
Madam -> True'''