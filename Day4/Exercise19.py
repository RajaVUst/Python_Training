def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
 
print(count_vowels("Python"))
print(count_vowels("The python programming Language is fun"))

# Output:
# 1
# 11