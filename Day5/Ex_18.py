names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]
report={name:score for name,score in zip(names,scores) if score>=70}
print(report)
#output
"""
{'Amit': 78, 'Reni': 91}
"""