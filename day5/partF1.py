def vowel_counts(sentence):
    words=sentence.split(" ")
    vowels="aeiouAEIOU"
    result={}
    
    for word in words:
        count=0
        for i in word:
            if i in vowels:
                count=count+1
        result[word]=count
    print(result)         
    
sentence="The Quick Brown Fox Jumps" 
vowel_counts(sentence)

# OUTPUT
# {'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}