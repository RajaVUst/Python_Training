def paliendrome_checker(text):
    reversed_text = text[::-1].lower()
    if(reversed_text==text.lower()):
        return True
    else:
        return False

print(paliendrome_checker("python"))
print(paliendrome_checker("level"))
print(paliendrome_checker("Madam"))

"""
Output->
False
True
True
"""