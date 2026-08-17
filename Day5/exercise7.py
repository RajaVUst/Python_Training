def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    average = sum(numbers) / len(numbers)

    return low, high, average


values = [9, 10, 12, 7, 15]

minimum, maximum, average = stats(values)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)



'''
Minimum: 7
Maximum: 15
Average: 10.6
'''