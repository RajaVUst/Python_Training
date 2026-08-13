#step1 If statement
age = 20

if age >= 18:
    print("You can vote")


#Step2  If - else statement

age = 15

if age >= 18:
    print("You can vote")
else:
    print("Not old enough yet")


#Step3 multiple elif
marks = 67

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


#step4

temperature = 33
is_raining = False
if temperature > 30 and not is_raining:
    print("Good day for a walk")
else:
    print("Maybe stay in")


#step 5

for i in range(1, 6):
    print(f"Iteration {i}")

#step 6
for n in range(1, 11):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")



