original = [1,2,3]
alias = original
safe_copy = original.copy()
alias.append(100)
safe_copy.append(200)
print(original)
print(alias)
print(safe_copy)
# original picked up 100 because alias refers to the same list, while safe_copy is a separate copy.