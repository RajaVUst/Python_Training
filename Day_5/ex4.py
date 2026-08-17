original = [1, 2, 3]

alias = original          # No copy, both names refer to the same list
safe_copy = original.copy()  # Creates a separate list

alias.append(100)
safe_copy.append(200)

print("original:", original)
print("alias:", alias)
print("safe_copy:", safe_copy)

# original changed when alias was modified because alias and original reference the 
# same list object; safe_copy is a separate list.

# Output
"""
original: [1, 2, 3, 100]
alias: [1, 2, 3, 100]
safe_copy: [1, 2, 3, 200]
"""