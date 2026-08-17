cart=['Soap','Chocolate','ToothPaste']
# Types to data to a list
cart.append('Comb')
cart.extend(['Pen','Pencil'])
print(cart)

print(cart.remove('ToothPaste'))
print(cart)

print(cart.index('Pen'))

# Before sorting
print(cart)
cart1=sorted(cart)  # or cart.sort()
print()
# After sorting
print(cart1)

# Output

"""['Soap', 'Chocolate', 'ToothPaste', 'Comb', 'Pen', 'Pencil']
None
['Soap', 'Chocolate', 'Comb', 'Pen', 'Pencil']
3
['Soap', 'Chocolate', 'Comb', 'Pen', 'Pencil']

['Chocolate', 'Comb', 'Pen', 'Pencil', 'Soap']"""