def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    avg = sum(numbers) / len(numbers)
    return low, high, avg


numbers = [4, 9, 1, 7, 15]

minimum, maximum, average = stats(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)


#output:
'''Minimum: 1
Maximum: 15
Average: 7.2'''