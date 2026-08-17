# Exercise 15: Squares and Cubes
cubes = [i**3 for i in range(1,11)]
evens = [i**3 for i in range(1,11) if i%2==0]

print(cubes)    # [1,8,27,64,125,216,343,512,729,1000]
print(evens)    # [8,64,216,512,1000]

# Exercise 16: Label the Temperatures
temps = [15,22,31,8,27,19]
temp = [ "hot" if i>=25 else "mild" if i>=15 else "cold" for i in temps]
print(temp)     # ['mild','mild','hot','cold','hot','mild']

# Exercise 17: Dictionary From Two Lists
names = ["Amit","Reni","Tara"]
scores = [78,91,65]
students = {name:score for name,score in zip(names,scores)}
print(students)     # {'Amit': 78, 'Reni': 91, 'Tara': 65}

# Exercise 18: Filtering with a Dict Comprehension
toppers = {name:score for name,score in students.items() if score >= 70}
print(toppers)      # {'Amit': 78, 'Reni': 91}