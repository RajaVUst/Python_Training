text = "the quick brown fox jumps over the lazy dog the fox runs"

words=text.split(" ")

words_count={}

for i in words:
    
        words_count[i]=words_count.get(i,0)+1

print(words_count)


# OUTPUT

# {'the': 3, 'quick': 1, 'brown': 1, 
# 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}