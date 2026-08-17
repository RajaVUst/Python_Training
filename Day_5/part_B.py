# Exercise 5

location = (12.97, 77.59) 
# print(locals)
# location[0]= 30.3

# tuple are immutable which means the value can't be changed 

# Excercise 6

record = ("Reni", 91, "Cohort 2")
name, score, cohort = record
print(f'{name} scored  {score} marks and belongs to {cohort}')

# Excercise 7 

def stats(number):
    minumum = min(number)
    maximum = max(number)
    average = sum(number) / len(number)
    return (minumum, maximum, average)
result = stats([4, 9, 1, 7, 15])
print(result)
minimum, maximum, average = result
print(f' minimum = {minimum}, maximu = {maximum}, average = {average}')