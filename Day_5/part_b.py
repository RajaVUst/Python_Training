# Exercise 5: Coordinates

location = (12.97, 77.59)

print("Original Location:", location)

try:
    location[0] = 13.00
except TypeError as e:
    print("Error:", e)




# Exercise 6: Unpacking Tuple

record = ("Reni", 91, "Cohort 2")

name, score, cohort = record

print(f"{name} scored {score} marks in {cohort}.")


# Exercise 7: Multiple Returns

def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    avg = sum(numbers) / len(numbers)

    return low, high, avg


numbers = [4, 9, 1, 7, 15]

minimum, maximum, average = stats(numbers)

print("Numbers :", numbers)
print("Minimum :", minimum)
print("Maximum :", maximum)
print(f"Average : {average:.2f}")