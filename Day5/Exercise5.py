
location = (12.97, 77.59)
try:
    location[0] = 13.0
except TypeError as e:
    print("Error raised:", e)
    
#output
# Error raised: 'tuple' object does not support item assignment