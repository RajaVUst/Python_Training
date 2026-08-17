original = [6,7,8]

alias = original
safe_copy = original.copy()

alias.append(100)
safe_copy.append(200)

print("Original:", original)
print("Alias:", alias)
print("Safe copy:", safe_copy)

'''
Original: [6, 7, 8, 100]
Alias: [6, 7, 8, 100]
Safe copy: [6, 7, 8, 200]
'''