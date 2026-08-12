# input a sentence
sentence = input("Enter a sentence: ")

# count the number of characters in the sentence
character_count = len(sentence)

# count the number of words in the sentence
word_count = len(sentence.split())

# count the number of vowels in the sentence
vowel_count = (
sentence.count('a') +
sentence.count('e') +
sentence.count('i') +
sentence.count('o') +
sentence.count('u')
)

# check if the sentence is longer than 30 characters
is_long = len(sentence) > 30

print("Character count: ", character_count)
print("Word count: ", word_count)
print("Vowel count: ", vowel_count)
print("Is the sentence longer than 30 characters: ", is_long)