squares=[n*n for n in range(1,21)]

word_lengths={word:len(word) for word in ['Java','C','Kotlin','Python','JavaScript']}

unique_vowels={ch for ch in 'the quick brown fox jumps over the lazy dog' if ch in 'aeiou'}

print("List of squares from 1 to 20:", squares)
print("Dictionary of word lengths:", word_lengths)  
print("Set of unique vowels in the sentence:", unique_vowels)

# Output:
# List of squares from 1 to 20: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
# Dictionary of word lengths: {'Java': 4, 'C': 1, 'Kotlin': 6, 'Python': 6, 'JavaScript': 10}
# Set of unique vowels in the sentence: {'e', 'o', 'i', 'a'}