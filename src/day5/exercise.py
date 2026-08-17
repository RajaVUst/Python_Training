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

text = "the quick brown fox jumps over the lazy dog the fox runs"

words = text.split()

word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts) #prints {'the': 2, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}

roster = [
    {
        "name": "Joel",
        "scores": [80, 90, 85]
    },
    {
        "name": "John",
        "scores": [70, 75, 80]
    },
    {
        "name": "David",
        "scores": [90, 95, 88]
    }
]

for student in roster:
    average = sum(student["scores"]) / len(student["scores"])

    print(student["name"], "Average:", round(average, 1)) #prints Joel Average: 85.0 John Average: 75.0 David Average: 91.0

grade_lookup = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

score = 84

if score >= grade_lookup["A"]:
    grade = "A"

elif score >= grade_lookup["B"]:
    grade = "B"

elif score >= grade_lookup["C"]:
    grade = "C"

elif score >= grade_lookup["D"]:
    grade = "D"

else:
    grade = "F"

print("Score:", score)
print("Grade:", grade) #prints B

#PART-E (Comprehensions)

list1 = [i**3 for i in range(1,11)]
print(list1) #prints [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

list2 = [i**3 for i in range(1,11) if i%2==0 ]
print(list2)

temps = [15, 22, 31, 8, 27, 19]

labels = ["hot" if t >= 25 else ("mild" if t >= 15 else "cold") for t in temps]

print(labels) #PRINTS ['mild', 'mild', 'hot', 'cold', 'hot', 'mild']

names = ["Amit", "Reni", "Tara"]
scores = [78, 91, 65]

scores_dict = {
    name: score
    for name, score in zip(names, scores)
}

print(scores_dict) #prints {'Amit': 78, 'Reni': 91, 'Tara': 65}

passing_scores = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}

print(passing_scores) #prints {'Amit': 78, 'Reni': 91}

#PART-F (Challenges)

def vowel_counts(sent):
    words = sent.split()

    result = {}

    for word in words:
        count = 0

        for ch in word:
            if ch.lower() in "aeiou":
                count = count + 1

        result[word] = count

    return result


sent = "The Quick Brown Fox Jumps"

print(vowel_counts(sent)) #prints {'The': 1, 'Quick': 2, 'Brown': 1, 'Fox': 1, 'Jumps': 1}

def grade_summary(roster):

    result = []

    for student in roster:

        average = sum(student["scores"]) / len(student["scores"])

        if average >= 90:
            grade = "A"

        elif average >= 80:
            grade = "B"

        elif average >= 70:
            grade = "C"

        elif average >= 60:
            grade = "D"

        else:
            grade = "F"

        new_student = {
            "name": student["name"],
            "average": round(average, 1),
            "grade": grade
        }

        result.append(new_student)

    return result


roster = [
    {
        "name": "Amit",
        "scores": [80, 85, 90]
    },
    {
        "name": "Reni",
        "scores": [95, 90, 92]
    },
    {
        "name": "Tara",
        "scores": [65, 70, 68]
    }
]

print(grade_summary(roster)) #prints [ {'name': 'Amit', 'average': 85.0, 'grade': 'B'},{'name': 'Reni', 'average': 92.3, 'grade': 'A'},{'name': 'Tara', 'average': 67.7, 'grade': 'D'}]

def unique_words(text):

    words = text.lower().split()

    unique = set(words)

    return sorted(unique)


text = "Python is easy and Python is powerful"

print(unique_words(text)) #prints ['and', 'easy', 'is', 'powerful', 'python']

def fizzbuzz_map(n):

    result = {}

    for i in range(1, n + 1):

        if i % 15 == 0:
            result[i] = "FizzBuzz"

        elif i % 3 == 0:
            result[i] = "Fizz"

        elif i % 5 == 0:
            result[i] = "Buzz"

        else:
            result[i] = str(i)

    return result


print(fizzbuzz_map(20)) 

def password_report(passwords):

    result = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for pw in passwords:

        has_digit = False

        for ch in pw:
            if ch.isdigit():
                has_digit = True

        if len(pw) >= 10 and has_digit:
            result["strong"].append(pw)

        elif len(pw) >= 6:
            result["medium"].append(pw)

        else:
            result["weak"].append(pw)

    return result


passwords = [
    "jojo",
    "python",
    "jojo@123",
    "MyPassword1",
    "hello12",
    "abcd"
]

print(password_report(passwords)) #prints { 'weak': ['jojo', 'abcd'],'medium': ['python', 'hello12'],'strong': ['jojo@123', 'MyPassword1']}
