
def vowel_counts(sentence):
    vowels = set("aeiou")
    result = {}
    for word in sentence.split():
        w = word.lower()
        result[word] = sum(1 for ch in w if ch in vowels)
    return result
 
print(vowel_counts("The Quick Brown Fox Jumps"))

#output
# {'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}