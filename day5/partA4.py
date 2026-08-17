original = [1, 2, 3]
alias=original
safe_copy=original.copy()
alias.append(100)
safe_copy.append(200)

print(f"original:{original}")
print(f"safe_copy:{safe_copy}")
print(f"alias:{alias}")


# OUTPUT

# original:[1, 2, 3, 100]
# safe_copy:[1, 2, 3, 200]
# alias:[1, 2, 3, 100]

# original changes with alias because both refer 
# to the same list, while safe_copy is a separate list.

