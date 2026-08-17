seen = set(range(1000))
if 999 in seen:
    print("999 is present")
else:
    print("999 is not present")
# A set is better than a list for repeated membership checks because set lookup is generally faster.
# output
# 999 is present