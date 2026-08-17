text = "the quick brown fox jumps over the lazy dog the fox runs"

word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
