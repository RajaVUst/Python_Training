original=[1,2,3]
alias=original
safe_copy=original.copy()
alias.append(100)
safe_copy.append(200)
print(original)
print(alias)
print(safe_copy)
#Output
"""
[1, 2, 3, 100]
[1, 2, 3, 100]
[1, 2, 3, 200]
because alias is just a second name pointing at the same list object as original
"""
