cart=["oil","Vegetable","Refiend Oil"]
cart.append("Atta")
cart.append("Maida")
print(f"After adding two item: {cart}")
cart.remove("oil")
print(f"After removig one item:{cart}")
cart1=sorted(cart)
print(f"after sorting :{cart1}")




#-----------EXERCISE 2---------------

queue = ["Amit", "Reni", "Tara", "Sam"]
queue.pop(0)
print(f" Before Appending:{queue}")
queue.append("Amit")
print(f" After Appending:{queue}")


#-----------EXERCISE 3---------------

readings = [12, 15, 9, 22, 30, 4, 18]
print(f"The First Three Elemet are:{readings[0:3]}")
print(f"The Last two Elemet are:{readings[-2:]}")
print(f"every second reading starting from index 0 is:{readings[::2]}")

#-----------EXERCISE 4---------------

original = [1, 2, 3]
alias = original
safe_copy = original.copy()
alias.append(100)
safe_copy.append(200)
print(f"orginal:{original}")
print(f"alias:{alias}")
print(f"safe_copy:{safe_copy}")

# original changed only with alias because alias
#  references the same list, while safe_copy is a separate copy.





