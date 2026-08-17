names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]
report={name:score for name,score in zip(names,scores)}
print(report)

#output
"""
{'Amit': 78, 'Reni': 91, 'Tara': 65}
"""