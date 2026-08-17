original = [1, 2, 3]

alias = original
safe_copy = original.copy()

alias.append(100)
safe_copy.append(200)

print(original)
print(alias)
print(safe_copy)

# output:
# [1, 2, 3, 100]
# [1, 2, 3, 100]
# [1, 2, 3, 200]
