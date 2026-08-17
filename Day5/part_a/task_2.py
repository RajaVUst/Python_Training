queue = ["Amit", "Reni", "Tara", "Sam"]
print(queue)

first_person = queue.pop(0)
print(queue)

queue.append(first_person)
print(queue)

# ['Amit', 'Reni', 'Tara', 'Sam']
# ['Reni', 'Tara', 'Sam']
# ['Reni', 'Tara', 'Sam', 'Amit']
