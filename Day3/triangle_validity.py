side1=int(input("enter the side1 value:"))
side2=int(input("enter the side2 value:"))
side3=int(input("enter the side3 value:"))
if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    print(f"It is a valid tringle")
else:
    print(f"This is not  valid tringle")