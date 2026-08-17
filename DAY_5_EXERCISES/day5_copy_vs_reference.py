original = [1, 2, 3]

alias = original
copy = original.copy()

alias.append(100)
copy.append(200)

print(original)
print(alias)
print(copy)

"""
Output->
[1, 2, 3, 100]
[1, 2, 3, 100]
[1, 2, 3, 200]
"""