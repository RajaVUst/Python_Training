# Vowel Counter by Word

def vowel_counts(sentence):
    words = sentence.lower().split()
    result = {}
    for word in words:
        count = 0
        for char in word:
            if char in "aeiou":
                count = count + 1
        result[word] = count

    return result


sentence = "The Quick Brown Fox Jumps"
print(vowel_counts(sentence))


# Output:
# {'the': 1, 'quick': 2, 'brown': 1, 'fox': 1, 'jumps': 1}