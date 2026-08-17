import statistics
#PART-A (Lists)

cart = ["Rice" , "Oil" , "Mat"]

cart.append("Knife")
cart.remove("Oil")
cart.remove("Mat")

print(sorted(cart)) #prints ['Knife', 'Rice']


queue = ["Amit", "Reni", "Tara", "Sam"]
print(f"Before : {queue}")

queue.append(queue.pop(0))
print(f"After : {queue}") #prints ['Reni', 'Tara', 'Sam', 'Amit']


readings = [12, 15, 9, 22, 30, 4, 18]

print(readings[0:3]) #prints [12, 15, 9]
print(readings[-2:]) #prints [4, 18]
print(readings[::2]) #prints [12, 9, 30, 18]

original = [1, 2, 3]
alias = original

safe_copy = original.copy()

alias.append(100)
safe_copy.append(200)

print(original) #prints [1, 2, 3, 100]
print(alias)    #prints [1, 2, 3, 100]
print(safe_copy)#prints [1, 2, 3, 200]

#original and alias are basically the same lists having diff names which points to a single list so they prints the same , using copy() creates a real copy of the list having diff ref

#PART-B (Tuples)

location = (12.97, 77.59) 

#location[0] = 99.99 prints TypeError: 'tuple' object does not support item assignment

record = ("Reni", 91, "Cohort 2")
name , score , cohort = record
print(f"The name is {name} and her score is {score} and {cohort}") #prints The name is Reni and her score is 91 and Cohort 2

def stats(numbers):
    low = min(numbers)
    high = max(numbers)
    avg =  statistics.mean(numbers)

    return low,high,avg 

print(stats([4, 9, 1, 7, 15])) #prints (1, 15, 7.2)

#PART-C (Sets)

attendance = ["amit", "reni", "amit", "tara", "reni", "sam"]

set1 = set(attendance) #prints 4

print(len(set1))

cohort_a = {"python", "sql", "excel"}
cohort_b = {"python", "tableau", "excel"}

print(cohort_a | cohort_b) #prints {'python', 'excel', 'sql', 'tableau'}
print(cohort_a - cohort_b) #prints {'sql'}
print(cohort_a & cohort_b) #prints {'excel', 'python'}


seen = set(range(1000))

if 999 in seen:
    print("999 is present in the set.") #prints this 
else:
    print("999 is not present in the set.")

# A set is better than a list here because membership checks are much faster for large collections.

#Part-D (Dictionaries)

contact = { "name" : "Joel" , "email" : "Joel15@gmail.com" , "Phone" : 9345555717}
print(f"He is {contact["name"]} , his email and phone number are {contact['email']} and {contact['Phone']}")

contact["city"] = "Kochi"
contact["Phone"] = 9898989898

contact.pop("email")
print(contact) #prints {'name': 'Joel', 'Phone': 9898989898, 'city': 'Kochi'}
