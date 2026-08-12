weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")