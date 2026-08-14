def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count


print(count_vowels("Python Bootcamp"))
print(count_vowels("Python programming is interesting"))

# output
# 4
# 9