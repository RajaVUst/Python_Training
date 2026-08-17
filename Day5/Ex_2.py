queue=["Amit","Reni","Tara","sam"]
print(queue)
removed=queue.pop(0)
queue.append(removed)
print(queue)
#output
"""
['Amit', 'Reni', 'Tara', 'sam']
['Reni', 'Tara', 'sam', 'Amit']
"""