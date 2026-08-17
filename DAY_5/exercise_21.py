def unique_words(text):
    return sorted(set(text.lower().split()))

print(unique_words("the cat sat on the mat and the cat napped"))
