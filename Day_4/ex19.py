def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count

print(count_vowels("Python Bootcamp"))
print(count_vowels("Learning Python is fun and useful!"))

#Output:
"""
4
10
"""