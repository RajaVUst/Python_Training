#Rotate the Queue
queue = ["Amit", "Reni", "Logesh", "Sam"]
print("Before:", queue)
first_person = queue.pop(0)
queue.append(first_person)
print("After:", queue)


# Output:
#Before: ['Amit', 'Reni', 'Logesh', 'Sam']
#After: ['Reni', 'Logesh', 'Sam', 'Amit']