def word_frequencies(path):
    frequencies = {}
 
    with open(path, "r") as f:
        text = f.read().lower()
 
    words = text.split()
 
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
 
    return frequencies
 
 
result = word_frequencies(r"Day_6\Ref doc\notes.txt")
 
print(result)
 
# Output:
# {'hello': 2, 'world': 1, 'python': 1}
 