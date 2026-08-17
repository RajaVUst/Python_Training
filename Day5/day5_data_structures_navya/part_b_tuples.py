# Exercise 5 - Coordinates
location = (12.97, 77.59)

location[0] = 13.05
# Output:
# TypeError: 'tuple' object does not support item assignment


# Exercise 6 - Unpacking a Tuple
record = ("Navya", 91, "Cohort 2")
name, score, cohort = record

print(f"{name} scored {score} marks and belongs to {cohort}")
# Output: Navya scored 91 marks and belongs to Cohort 2


# Exercise 7 - Multiple Return Values
def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    avg = sum(numbers) / len(numbers)
    return low, high, avg

numbers = [4, 9, 1, 7, 15]
minimum, maximum, average = stats(numbers)

print(minimum, maximum, average)
# Output: 1 15 7.2