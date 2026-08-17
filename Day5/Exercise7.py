
def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    avg = sum(numbers) / len(numbers)
    return low, high, avg
 
minimum, maximum, average = stats([4, 9, 1, 7, 15])
print(f"min={minimum}, max={maximum}, avg={average}")

#output
# min=1, max=15, avg=7.2