def vowel_counts(sentence):
    vowels="aeiou"
    res={}
    for i in sentence.split():
        count=0
        for j in range(len(i)):
            if i[j].lower() in vowels:
                count+=1
        res[i]=count
    return res 
sentence="The Quick Brown Fox Jumps"
print(vowel_counts(sentence))
#output
"""
{'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}
"""

