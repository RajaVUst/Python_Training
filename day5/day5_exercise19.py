def vowel_counts(sentence):
    result = {}

    for word in sentence.split():
        count = 0

        for char in word.lower():
            if char in "aeiou":
                count += 1

        result[word] = count

    return result


print(vowel_counts("The Quick Brown Fox Jumps"))

"""
OUTPUT:
{'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}
"""