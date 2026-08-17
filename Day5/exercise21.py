def unique_words(text):
    words = text.lower().split()
    unique = set(words)

    return sorted(unique)


sentence = "Python is useful and Python is easy"

print(unique_words(sentence))

'''
output

['and', 'easy', 'is', 'python', 'useful']

'''