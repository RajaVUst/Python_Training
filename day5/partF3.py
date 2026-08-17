def unique_words(text):
    words=text.lower().split(" ")
    word_sorted=sorted(words)
    
    print(set(word_sorted))
    
text="hello hello i am Bonny"
unique_words(text)


# OUTPUT
# {'hello', 'i', 'am', 'bonny'}