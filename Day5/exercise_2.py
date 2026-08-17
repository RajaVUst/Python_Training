queue = ["Amit", "Reni", "Tara", "Sam"]
print("Before:", queue)
person = queue.pop(0)
queue.append(person)
print("After:", queue)

# output
# Before: ['Amit', 'Reni', 'Tara', 'Sam']
# After: ['Reni', 'Tara', 'Sam', 'Amit']