# Exercise 5: Coordinates
location = (12.97, 77.59)
#location[0] = 56.62     # TypeError: 'tuple' object does not support item assignment

# Exercise 6: Unpacking a Tuple
record = ("Reni", 91, "Cohort 2")
name, score, cohort = record
print(f"Name: {name}, Score: {score}, Cohort: {cohort}")    # Name: Reni, Score: 91, Cohort: Cohort 2

# Exercise 7: Multiple Return Values
def stats(numbers):
    return (min(numbers), max(numbers), sum(numbers)/len(numbers))

minn, maxx, avg = stats([4, 9, 1, 7, 15])
print(f"Min: {minn}, Max: {maxx}, Average: {avg}")      # Min: 1, Max: 15, Average: 7.2