def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    avg = sum(numbers) / len(numbers)
    return low, high, avg

# Call the function and unpack the result
minimum, maximum, average = stats([4, 9, 1, 7, 15])

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {average}")

# Output:
"""Minimum: 1
Maximum: 15     
Average: 7.2"""