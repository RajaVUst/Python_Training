
queue = ["Amit", "Reni", "Tara", "Sam"]
print("Before:", queue)
first = queue.pop(0)
queue.append(first)
print("After:", queue)

#output
# Before: ['Amit', 'Reni', 'Tara', 'Sam']
# After: ['Reni', 'Tara', 'Sam', 'Amit']