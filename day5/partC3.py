seen = set(range(1000))

if 999 in seen:
    print("999 is present in the set")
else:
    print("999 is not present in the set")
    
    # A set is better than a list for repeated membership 
    # checks because lookup is generally much faster.
    
    # OUTPUT
    
    # 999 is present in the set