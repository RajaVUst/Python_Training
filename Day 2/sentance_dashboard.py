sentence = input("Enter a sentence: ")
print("Character count:", len(sentence))
print("Word count:", len(sentence.split()))
print("Vowel count:",
      sentence.count('a') +
      sentence.count('e') +
      sentence.count('i') +
      sentence.count('o') +
      sentence.count('u'))
print("Longer than 30 characters:", len(sentence) > 30)