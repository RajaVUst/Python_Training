def vowel_counts(sentence):
    words = sentence.lower().split()
    result = {}

    for word in words:
        count = sum(1 for char in word if char in "aeiou")
        result[word] = count

    return result

print(vowel_counts("The Quick Brown Fox Jumps"))

# output:
# {'the': 1, 'quick': 2, 'brown': 1, 'fox': 1, 'jumps': 1}