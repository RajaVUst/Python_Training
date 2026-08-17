queue = ["Deepa", "Sruthie", "Varsha", "Pranav"]

print("Before:", queue)

first_person = queue.pop(0)
queue.append(first_person)

print("After:", queue)


#output:
'''Before: ['Deepa', 'Sruthie', 'Varsha', 'Pranav']
After: ['Sruthie', 'Varsha', 'Pranav', 'Deepa']'''