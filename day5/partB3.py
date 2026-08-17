def stat(numbers):
    maximum,minimum,average=max(numbers),min(numbers),sum(numbers)/len(numbers)
    return (maximum,minimum,average)

tuple=[4, 9, 1, 7, 15] 

minimum, maximum, average = stat(tuple)

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {average}")

# OUTPUT

# Minimum: 15
# Maximum: 1
# Average: 7.2