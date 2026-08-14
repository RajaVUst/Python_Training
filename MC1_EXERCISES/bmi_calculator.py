height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)

print(f"Your BMI index is {bmi:.1f}")

"""
Output ->
Enter your height in meters: 1.6
Enter your weight in kg: 55
Your BMI index is 21.5
"""