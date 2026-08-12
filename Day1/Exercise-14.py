# Exercise 14 — Student Report Line
marks_1 = float(input("Enter test score 1: "))
marks_2 = float(input("Enter test score 2: "))
marks_3 = float(input("Enter test score 3: "))

avg_marks = (marks_1 + marks_2 + marks_3) / 3
passed_status = (avg_marks >= 40)

print(f"Average: {avg_marks:.1f} | Passed: {passed_status}")