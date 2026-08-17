# Part A: Lists

# Exercise 1: Shopping List Manager
cart = ["Milk", "Bread", "Eggs"]
cart.append("Rice")
cart.append("Apple")
cart.remove("Bread")
print("Original cart:", cart)
print("Sorted cart:", sorted(cart))
# Output:
# Original cart: ['Milk', 'Eggs', 'Rice', 'Apple']
# Sorted cart: ['Apple', 'Eggs', 'Milk', 'Rice']
print("\n" + "="*40 + "\n")

# Exercise 2: Rotate the Queue
queue = ["Amit", "Reni", "Tara", "Sam"]
print("Before rotation:", queue)
person = queue.pop(0)
queue.append(person)
print("After rotation:", queue)
# Output:
# Before rotation: ['Amit', 'Reni', 'Tara', 'Sam']
# After rotation: ['Reni', 'Tara', 'Sam', 'Amit']
print("\n" + "="*40 + "\n")

# Exercise 3: Running Total With Slicing
readings = [12, 15, 9, 22, 30, 4, 18]
print("First three readings:", readings[:3])
print("Last two readings:", readings[-2:])
print("Every second reading:", readings[::2])
# Output:
# First three readings: [12, 15, 9]
# Last two readings: [4, 18]
# Every second reading: [12, 9, 30, 18]
print("\n" + "="*40 + "\n")

# Exercise 4: Copy vs. Reference
original = [1, 2, 3]
alias = original
safe_copy = original.copy()
alias.append(100)
safe_copy.append(200)
print("Original:", original)
print("Alias:", alias)
print("Safe Copy:", safe_copy)
# Output:
# Original: [1, 2, 3, 100]
# Alias: [1, 2, 3, 100]
# Safe Copy: [1, 2, 3, 200]
print("\n" + "="*40 + "\n")