# Exercise 6 - Sentence Dashboard
sentence = "python is easy and fun to learn"
character_count = len(sentence)
word_count = len(sentence.split())
vowel_count = (
    sentence.count("a")
    + sentence.count("e")
    + sentence.count("i")
    + sentence.count("o")
    + sentence.count("u")
)
longer_than_30 = len(sentence) > 30

print(f"Character Count: {character_count}")
print(f"Word Count: {word_count}")
print(f"Vowel Count: {vowel_count}")
print(f"Longer Than 30 Characters: {longer_than_30}")