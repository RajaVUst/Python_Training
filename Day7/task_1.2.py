# List comprehension

squares = [n * n for n in range(1, 21) if n % 2 == 0]
print(squares)

# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


# Dictionary comprehension

word_lengths = {
    word: len(word)
    for word in ["python", "java", "c", "kotlin"]
}

print(word_lengths)

# {'python': 6, 'java': 4, 'c': 1, 'kotlin': 6}


# Set comprehension
unique_vowels = {
    ch
    for ch in "the quick brown fox jumps over the lazy dog"
    if ch in "aeiou"
}

print(unique_vowels)


# {'e', 'u', 'a', 'i', 'o'}