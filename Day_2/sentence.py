sentence = 'python is fun to learn'
print(f'character count: {len(sentence)}', )
print(f'word count: {len(sentence.split())}')
vowels = sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
print(f'Vowl count : {vowels}')
print(f'longer than 30 characters {len(sentence) > 30}')