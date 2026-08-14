def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
        
student_info(name="Bonny",age="22",course="Python",city="TVM")

# OUTPUT

# name:Bonny
# age:22
# course:Python
# city:TVM