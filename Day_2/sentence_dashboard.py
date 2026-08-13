sentence = "Python is fun and easy to learn"

character_count = len(sentence)
word_count = len(sentence.split())
vowel_count = (
    sentence.count('a') +
    sentence.count('e') +
    sentence.count('i') +
    sentence.count('o') +
    sentence.count('u')
)

is_long = len(sentence) > 30

print("Character count:", character_count)
print("Word count:", word_count)
print("Vowel count:", vowel_count)
print("Longer than 30 characters:", is_long)