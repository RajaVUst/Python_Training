text = "the quick brown fox jumps over the lazy dog the fox runs"
dict1={}
for i in text.split():
    dict1[i]=dict1.get(i,0)+1
print(dict1)
#output
"""
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}
"""
