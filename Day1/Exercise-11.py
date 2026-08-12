# Exercise 11 — BMI Calculator
weight_kg = float(input("Enter weight in kg: "))
height_m = float(input("Enter height in metres: "))

bmi_value = weight_kg / (height_m ** 2)
print(f"BMI: {bmi_value:.1f}")