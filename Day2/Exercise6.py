#Sentence Dashboard
sentence = "The quick brown fox jumps over the lazy dog"
char_count = len(sentence)
word_count = len(sentence.split())
vowel_count = (sentence.count('a') + sentence.count('e') + sentence.count('i')
               + sentence.count('o') + sentence.count('u'))
is_long = len(sentence) > 30

print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"Vowels: {vowel_count}")
print(f"Longer than 30 chars: {is_long}")