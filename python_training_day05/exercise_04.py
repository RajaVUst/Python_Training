original = [1, 2, 3]

alias = original
safe_copy = original.copy()

alias.append(100)
safe_copy.append(200)

print("Original:", original)
print("Alias:", alias)
print("Safe copy:", safe_copy)


#output:
'''Original: [1, 2, 3, 100]
Alias: [1, 2, 3, 100]
Safe copy: [1, 2, 3, 200]'''