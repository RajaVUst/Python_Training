# Exercise 11 - BMI Calculator
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))
bmi = weight / (height ** 2)

print(f"BMI: {bmi:.1f}")