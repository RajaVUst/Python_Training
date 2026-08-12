sentence = input("Enter a sentence: ")

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

print(f"Character count: {character_count}")
print(f"Word count: {word_count}")
print(f"Vowel count: {vowel_count}")
print(f"Longer than 30 characters: {longer_than_30}")