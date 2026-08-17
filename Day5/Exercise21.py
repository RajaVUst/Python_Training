
def unique_words(text):
    words = {w.lower() for w in text.split()}
    return sorted(words)
 
print(unique_words("the fox and the hound and the cat"))

#output
# ['and', 'cat', 'fox', 'hound', 'the']