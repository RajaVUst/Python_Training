# accept weight in kg and height in m
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))

# calculate BMI and print the result
bmi = weight / (height ** 2)
print(f"BMI is {bmi:.1f}")