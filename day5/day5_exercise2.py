queue = ["Aron", "Pranav", "Aswin", "Chris"]

print("Before:", queue)

first_person = queue.pop(0)
queue.append(first_person)

print("After:", queue)

"""
OUTPUT:
Before: ['Aron', 'Pranav', 'Aswin', 'Chris']
After: ['Pranav', 'Aswin', 'Chris', 'Aron']
"""