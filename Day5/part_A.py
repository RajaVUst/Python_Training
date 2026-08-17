# Exercise 1: Shopping List Manager
groceries = ['Fruits', 'Vegies', 'Pulses']
groceries.append('Grains')
groceries.append('Liquids')
groceries.remove('Vegies')
print(sorted(groceries))    # ['Fruits', 'Grains', 'Liquids', 'Pulses']

# Exercise 2: Rotate the Queue
queue = ["Amit", "Reni", "Tara", "Sam"]
print("List before", queue)    # List before ['Amit', 'Reni', 'Tara', 'Sam']
queue.append(queue.pop(0))
print("List After", queue)     # List After ['Reni', 'Tara', 'Sam', 'Amit']

# Exercise 3: Running Total With Slicing
readings = [12, 15, 9, 22, 30, 4, 18]
print(readings[:3])         # [12, 15, 9]
print(readings[-2:])        # [4, 18]
print(readings[0::2])       # [12, 9, 30, 18]

# Exercise 4: Copy vs. Reference
original = [1, 2, 3]
alias = original
safe_copy = original.copy()
alias.append(100)
safe_copy.append(200)
# alias points to same as original but safe_copy creates new list after appending
print("Original", original)     # Original [1, 2, 3, 100]
print("Alias", alias)           # Alias [1, 2, 3, 100]
print("Safe copy", safe_copy)   # Safe copy [1, 2, 3, 200]