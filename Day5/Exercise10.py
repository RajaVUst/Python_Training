
seen = set(range(1000))
if 999 in seen:
    print("999 is in seen")
else:
    print("999 is NOT in seen")

#output
# 999 is in seen
# A set gives O(1) average-time membership checks (via hashing), while a
# list requires an O(n) scan; for thousands of repeated checks a set is
# dramatically faster.