def vowel_counts(sentence):
    vowels = "aeiou"
    result = {}

    for word in sentence.split():
        count = 0

        for character in word.lower():
            if character in vowels:
                count += 1

        result[word] = count

    return result


sentence = "The Quick Brown Fox Jumps"
print(vowel_counts(sentence))

'''
output

{'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}

'''