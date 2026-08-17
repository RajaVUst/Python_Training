# Fast Membership Check

seen = set(range(1000))

if 999 in seen:
    print("999 is present")
else:
    print("999 is not present")


# Output:
# 999 is present
# A set is better than a list because checking whether an element exists is much faster in a set.