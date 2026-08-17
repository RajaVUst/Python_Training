def vowel_counts(sentence):
    words = sentence.lower().split()
    result = {}

    for word in words:
        count = 0

        for ch in word:
            if ch in "aeiou":
                count += 1

        result[word] = count

    return result


sentence = "The Quick Brown Fox Jumps"

print(vowel_counts(sentence))


# {'the': 1, 'quick': 2, 'brown': 1, 'fox': 1, 'jumps': 1}