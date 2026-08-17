queue = ["Amit", "Reni", "Tara", "Sam"]

print("Before:", queue)
first_person = queue.pop(0)
queue.append(first_person)

print("After:", queue)

# output:
# Before: ['Amit', 'Reni', 'Tara', 'Sam']
# After: ['Reni', 'Tara', 'Sam', 'Amit']