students={"Yesh":[20,10,40],"Arun":[60,80,90],"Rohith":[50,30,20]}
for key,val in students.items():
    print(f"{key} {sum(val)//3:.1f}")

#output
"""
Yesh 23.0
Arun 76.0
Rohith 33.0
"""