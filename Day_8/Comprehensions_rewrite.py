squares = [n * n for n in range(1, 21) if n % 2 == 0]
word_lengths = {
    word: len(word)
    for word in ["python", "java", "c", "kotlin"]
}
unique_vowels = {
    ch
    for ch in "the quick brown fox jumps over the lazy dog"
    if ch in "aeiou"
}
print("Squares of even numbers:", squares)
print("Word lengths:", word_lengths)
print("Unique vowels:", unique_vowels)

# output:
# Squares of even numbers: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
# Word lengths: {'python': 6, 'java': 4, 'c': 1, 'kotlin': 6}
# Unique vowels: {'o', 'i', 'a', 'u', 'e'}