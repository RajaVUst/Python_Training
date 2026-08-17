text = "the quick brown fox jumps over the lazy dog the fox runs"
text_list = text.split()
counter = {}

for word in text_list:
    if word in counter:
        counter[word]+=1
    else:
        counter[word]=1

print(counter)

"""
Output->
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}"""

