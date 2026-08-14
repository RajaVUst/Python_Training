def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count

print(count_vowels("Python Bootcamp"))
print(count_vowels("Hello, how are you today?"))

# output:
# 4
# 9