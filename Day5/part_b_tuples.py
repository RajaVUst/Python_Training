# Part B: Tuples

# Exercise 5: Coordinates
location = (12.97, 77.59)
print("Original Location:", location)
# Trying to modify a tuple element
# location[0] = 13.00

# Output:
# Original Location: (12.97, 77.59)
# If location[0] = 13.00 is uncommented:
# TypeError: 'tuple' object does not support item assignment
# Reason:Tuples are immutable, meaning their values cannot be changed after creation.
print("\n" + "="*40 + "\n")


# Exercise 6: Unpacking a Tuple
record = ("Reni", 91, "Cohort 2")
name, score, cohort = record
print(f"{name} scored {score} marks and belongs to {cohort}.")
# Output:
# Reni scored 91 marks and belongs to Cohort 2.
print("\n" + "="*40 + "\n")


# Exercise 7: Multiple Return Values
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
# Output:
# Minimum: 1
# Maximum: 15
# Average: 7.2