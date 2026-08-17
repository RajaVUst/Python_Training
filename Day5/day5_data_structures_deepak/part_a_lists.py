# Exercise 1 - Shopping List Manager
cart = ["milk", "bread", "eggs"]
cart.append("butter")
cart.append("cheese")
cart.remove("bread")
print(sorted(cart))
# Output: ['butter', 'cheese', 'eggs', 'milk']
 
# Exercise 2 - Rotate the Queue
queue = ["Amit", "Reni", "Tara", "Sam"]
print(queue)
 
first_person = queue.pop(0)
queue.append(first_person)
print(queue)
# Output:
# ['Amit', 'Reni', 'Tara', 'Sam']
# ['Reni', 'Tara', 'Sam', 'Amit']
 
# Exercise 3 - Running Total With Slicing
readings = [12, 15, 9, 22, 30, 4, 18]
print(readings[:3])
print(readings[-2:])
print(readings[::2])
# Output:
# [12, 15, 9]
# [4, 18]
# [12, 9, 30, 18]
 
# Exercise 4 - Copy vs Reference
original = [1, 2, 3]
alias = original
safe_copy = original.copy()
 
alias.append(100)
safe_copy.append(200)
 
print(original)
print(alias)
print(safe_copy)
# Output:
# [1, 2, 3, 100]
# [1, 2, 3, 100]
# [1, 2, 3, 200]
# alias is the same list as original, safe_copy is a separate one