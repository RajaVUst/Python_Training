queue = ["Sai", "aishwarya", "vignesh", "Sam"]

print("Before:", queue)

first_person = queue.pop(0)
queue.append(first_person)

print("After:", queue)

'''
Before: ['Sai', 'aishwarya', 'vignesh', 'Sam']
After: ['aishwarya', 'vignesh', 'Sam', 'Sai']
'''