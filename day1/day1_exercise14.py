# accept scores for three tests
test_1 = float(input("Enter test score 1: "))
test_2 = float(input("Enter test score 2: "))
test_3 = float(input("Enter test score 3: "))

# calculate average and determine if the student has passed
average = (test_1 + test_2 + test_3) / 3
has_passed = average >= 40

# print the results
print(f"Average: {average:.1f} | Passed: {has_passed}")