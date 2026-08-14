def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    return count


print(count_vowels("Python Bootcamp"))
print(count_vowels("I am learning Python"))

'''
4
6
'''