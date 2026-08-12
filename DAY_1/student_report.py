m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))

average = (m1+m2+m3)/3

has_passed = (average>40)
print(f"Average: {average:.1f}")
print(f"Passed: {has_passed:}")