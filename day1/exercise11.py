weight=float(input("enter the weight in kilograms"))
height=float(input("enter the height in meters "))

bmi=weight/(height ** 2)

print(f"Your BMI is: {bmi:.1f}")