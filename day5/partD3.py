rooster=[
    
    {"name":"Bonny","scores":[40,50,60]},
    {"name":"vinaya","scores":[55,66,77]},
    {"name":"arjun","scores":[56,67,78]}
]

for i in rooster:
    total=sum(i["scores"])
    avg=total/len(i["scores"])
    
    print(f"{i["name"]} average score={avg:.1f}")
    
# OUTPUT

# Bonny average score=50.0
# vinaya average score=66.0
# arjun average score=67.0