#Multiple Return Values
def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    average = sum(numbers) / len(numbers)

    return low, high, average

result = stats([4, 9, 1, 7, 15])
minimum, maximum, average = result

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)


# Output:
# Minimum: 1
# Maximum: 15
# Average: 7.2