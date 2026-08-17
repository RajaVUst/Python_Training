# Exercise 1: Shopping List Manager

cart = ["Milk", "Bread", "Eggs"]

cart.append("Rice")
cart.append("Apples")

cart.remove("Bread")

print(cart)
print(sorted(cart))


# Exercise 2: Rotate Queue

queue = ["Amit", "Reni", "Tara", "Sam"]

print(queue)

person = queue.pop(0)
queue.append(person)

print(queue)


# Exercise 3: Running Total Slicing

readings = [12, 15, 9, 22, 30, 4, 18]

print("First three readings:", readings[:3])
print("Last two readings:", readings[-2:])
print("Every second reading:", readings[::2])


# Exercise 4: Copy vs Reference

original = [1, 2, 3]

alias = original
safe_copy = original.copy()

alias.append(100)
safe_copy.append(200)

print("Original :", original)
print("Alias    :", alias)
print("Safe Copy:", safe_copy)
