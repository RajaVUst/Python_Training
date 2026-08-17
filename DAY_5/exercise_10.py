seen = set(range(1000))
print(seen)
if 999 in seen:
    print("999 is in the set.")
else:
    print("999 is not in the set.")

# Sets use a hash table internally, so membership checks are O(1) regardless of size,
# while a list requires scanning every element (O(n)) — sets are far faster for repeated lookups.
