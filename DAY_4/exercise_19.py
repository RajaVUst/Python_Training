def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Python Bootcamp"))          # Expected: 4
print(count_vowels("The quick brown fox"))      # Expected: 5
