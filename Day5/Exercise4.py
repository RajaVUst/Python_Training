
original = [1, 2, 3]
alias = original                
safe_copy = original.copy()     
alias.append(100)
safe_copy.append(200)
print("original:", original)
print("alias:", alias)
print("safe_copy:", safe_copy)

#output
# original: [1, 2, 3, 100]
# alias: [1, 2, 3, 100]
# safe_copy: [1, 2, 3, 200]
# original picked up the alias change (100) because alias points to the
# SAME list object as original, but not the safe_copy change (200)
# because safe_copy is an independent copy of the list.