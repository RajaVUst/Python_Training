seen = set(range(1000))

if 999 in seen:
    print("999 has been seen.")
else:
    print("999 has not been seen.")

# Sets are better than lists for frequent membership checks 
# because lookup is typically much faster, especially for large collections.

# Output:
# 999 has been seen.