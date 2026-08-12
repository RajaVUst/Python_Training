# Exercise 8 — Rectangle Calculator
rect_length = float(input("Enter rectangle length: "))
rect_width = float(input("Enter rectangle width: "))

rect_area = rect_length * rect_width
rect_perimeter = 2 * (rect_length + rect_width)
print(f"Area: {rect_area}")
print(f"Perimeter: {rect_perimeter}")