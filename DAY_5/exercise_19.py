def vowel_counts(sentence):
    vowels = "aeiou"
    result = {}
    for word in sentence.split():
        count = 0
        for ch in word.lower():
            if ch in vowels:
                count += 1
        result[word] = count
    return result

print(vowel_counts("The Quick Brown Fox Jumps"))
