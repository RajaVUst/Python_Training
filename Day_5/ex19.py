def vowel_counts(sentence):
    vowels = "aeiou"

    return {word: sum(1 for ch in word.lower() if ch in vowels) for word in sentence.split() }

result = vowel_counts("The Quick Brown Fox Jumps")
print(result)

# Output:
# {'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}
