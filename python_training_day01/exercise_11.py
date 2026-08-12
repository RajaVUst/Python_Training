weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in metres: "))

bmi = weight / (height ** 2)

print(f"BMI: {bmi:.1f}")