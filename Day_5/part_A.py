# Excercise 1

cart = ['Milk', 'salt', 'detergent']
print(type(cart))
cart.append('egg')
cart.append('curd')
print(cart)
cart.remove('egg')
print(cart)
# cart.sort()
cart1 = sorted(cart)
print(cart1)

#out put

# <class 'list'>
# ['Milk', 'salt', 'detergent', 'egg', 'curd']
# ['Milk', 'salt', 'detergent', 'curd']
# ['Milk', 'curd', 'detergent', 'salt']

# Excercise 

queue = ["Amit", "Reni", "Tara", "Sam"]
queue.pop(0)
print(queue)
queue.append('Amit')
print(queue)

# Exercise 3 

readings = [12, 15, 9, 22, 30, 4, 18]
print(readings[:3])
print(readings[-2:])
print(readings[::2])


# Excercise 4

original = [1, 2, 3]
alias = original
safe_copy = original.copy()

alias.append(100)
safe_copy.append(200)
print('orginal:', original)
print('alias:', alias)
print('safe copy', safe_copy)