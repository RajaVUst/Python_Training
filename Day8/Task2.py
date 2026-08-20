squares=[n*n for n in range(1,21) if n%2==0]
word_lengths={word:len(word) for word in ["python", "java", "c", "kotlin"]}
unique_vowels={ch for ch in "the quick brown fox jumps over the lazy dog" if ch in "aeiou"}
print(squares)
print(word_lengths)
print(unique_vowels)
#output
"""[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
{'python': 6, 'java': 4, 'c': 1, 'kotlin': 6}
{'o', 'u', 'i', 'a', 'e'}
"""