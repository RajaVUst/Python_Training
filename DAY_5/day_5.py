#1
# groc=["sugar","mlk","curd"]
# groc.append("oil")
# groc.append("chilly")
# groc.remove("oil")
# #groc.sort()
# print(f" UN Sorted grocires list:{groc}")
# print(f"Sorted grocires list:{sorted(groc)}")


#2
# data= ["Amit", "Reni", "Tara", "Sam"]
# print("Before",data)
# data.pop(0)

# data.append("Amit")
# print("After",data)


#3
# readings = [12, 15, 9, 22, 30, 4, 18]
# print(f"first three readings{readings[:3]}")
# print(f"Last two  readings{readings[-2:]}")
# print(f"Every second readings{readings[::2]}")

#4
# original=[1,2,3]
# alias=original
# safe_copy=original.copy()
# alias.append(100)
# safe_copy.append(200)
# print("Alias:",alias)
# print("Copy:",safe_copy)
# print("Original:",original)
# print("alias and original point to the same list, so original also gets 100, but safe_copy is a separate list.")


#5
# location = (12.97, 77.59) 
# location[0]=12.00
# print(location)


#6
# record = ("Reni", 91, "Cohort 2")
# name, score, cohort= record
# print(f"Name:{name}, Score:{score}, Cohort:{cohort}")

#7
# def stat(numbers):
#     average=sum(numbers)/len(numbers)
#     return min(numbers), max(numbers), average
    
# record=tuple(map(int,input("enter the values:").split()))
# min_value,max_value,avg=stat(record)
# print(f"Minimum value:{min_value}")
# print(f"Maximum value:{max_value}")
# print(f"Average :{avg}")    

# #8
# attendence=["amit", "reni", "amit", "tara", "reni", "sam"]
# att=set(attendence)
# coun_att=len(att)
# print(f"count of attendes before removing dupicates:{attendence} is {len(attendence)}")
# print(f"count of attendes after removing duplicates:{att} is {coun_att}")


#9
# cohort_a = {"python", "sql", "excel"}  
# cohort_b = {"python", "tableau", "excel"}
# print(f"Skills common to both cohorts:{cohort_a & cohort_b}")
# print(f"the skills unique to cohort_a:{cohort_a - cohort_b}")
# print(f" ALL Skills from  both cohorts:{cohort_a | cohort_b}")


# #10
# seen=set(range(1000))
# if 999 in seen:
#     print("999 is presen in the seen ")
# else:
#     print("999 is not present in seen")   
# ## A set is better than a list because membership checks are much faster for large collections.     

# #11
# data={'name':"surenda",'email':"sure@gamil.com", 'phone':61263453416}
# print(data)
# data['city']="hyd"
# data['phone']=7643763673473463
# print(data)
# data.pop('email')
# print(data)

#12
# text = "the quick brown fox jumps over the lazy dog the fox runs"
# text=text.split()
# word_count={}
# for word in text:
    
#     word_count[word]=word_count.get(word,0)+1
# print(word_count)
 

 #13
# records=[
#     {'name':"Surendr",'score':[56,67,90]},
#     {'name':"ram",'score':[54,57,50]},
#     {'name':"nag",'score':[56,57,90]}
#  ]

# for student in records:
#     average=sum(student['score'])/len(student['score'])
#     print(f"{student['name']}->{average:.1f}")


# #14
# grade_lookup={
#     "A":90,
#     "B":80,
#     "C":70,
#     "D":60,
#     "F":0

# }
# score=int(input("ENter the score:"))
# for grade, minimum in grade_lookup.items():
#     if score>=minimum:
#         print("Grade:",grade)
#         break


#15
# n=int(input("Enter the number:"))
# # result=[i**3 for i in range(1,n+1)]
# # print(f"Cubes from 1 to 10:{result}")
# # result=[i**3 for i in range(1,n+1) if i%2==0]
# # print(f"Even cubes from 1 to 10:{result}")

#16
# temperature= [15, 22, 31, 8, 27, 19]
# result=[f"{temp}-> {"hot" if temp>=25 else ("mild" if temp>=15 else "cold")}" for temp in temperature]
# print(result)


# #17
# names = ["Amit", "Reni", "Tara"]
# scores = [78, 91, 65]
# result={ name:score for name,score in zip(names,scores)}
# print(result)



#18


# names = ["Amit", "Reni", "Tara"]
# scores = [78, 91, 65]
# result={ name:score for name,score in zip(names,scores) }
# print(result)


# score_dict={name:score for name,score in zip(names,scores)}
# result={name:score for name ,score in score_dict.items()if score>=70}
# print(result)

# def vowel_count(sentence):
#     words=sentence.split()
#     result={}
#     for word in words:
#         count=0
#         for ch in word.lower():
#             if ch in 'aeiou':
#                 count+=1
#         result[word]=count
#     return result          
# sentence=input("ENter the sentence")    
# print(vowel_count(sentence))



# def vowel_count(senetence):
#     words=senetence.split()
#     return {
#       word:sum  (1 for ch in word.lower() if ch in 'aeiou') for word in words
#     }
# senetence=input("Enter the sentence:")
# print(vowel_count(senetence))
    

#20
# def grade_summary(roster):
#     result=[]
#     for student in roster:
#         average=sum(student["scores"])/len(student["scores"])
#         if average>=90:
#             grade="A"
#         elif average>=80:
#             grade="B"
#         elif average>=70:
#             grade="C"
#         elif average>=60:
#             grade="D"
#         else:
#             grade="F"
#         result.append({"name":student['name'],
#         "average:":f"{average:.2f}",
#         "Grade":grade})
#     return result             


# roster=[
#     {'name':"surendra",'scores':[56,76,98]},
#     {'name':"prem",'scores':[87,98,65]},
#     {'name':"ram",'scores':[98,65,43]},
# ]        

# print(grade_summary(roster))



#21
# def unique_words(text):
#     senetence=text.lower().split()
#     result=set(senetence)
#     return sorted(result)
# text=input("Enter the text:")
# print(unique_words(text))     


#22
# def fizzbuzz_map(n):
#     result={}
#     for i in range(1, n+1):
#         if i%3==0 and i%5==0:
#             result[i]="FizzBuzz"
#         elif i%3==0:
#             result[i]="Fizz"
#         elif i%5==0:
#             result[i]="Buzz"
#         else:
#             result[i]=str(i)
#     return result                

# n=int(input("ENtehr the number"))    
# print(fizzbuzz_map(n))

#23
def password_report(passwords):
    result = {
        "weak": [],
        "medium": [],
        "strong": []
    }

    for pw in passwords:
        if len(pw) < 6:
            result["weak"].append(pw)

        elif len(pw) >= 10 and any(ch.isdigit() for ch in pw):
            result["strong"].append(pw)

        else:
            result["medium"].append(pw)

    return result


passwords = [
    "abc",
    "hello",
    "python",
    "python123",
    "MyPassword1",
    "abcdef123456"
]

print(password_report(passwords))