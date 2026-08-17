def vowel_counts(sentence):
    vowels = "aeiou"
    return {
        word: sum(1 for ch in word.lower() if ch in vowels)
        for word in sentence.split()
    }

print(vowel_counts("The Quick Brown Fox Jumps"))
