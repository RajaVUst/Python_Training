#1
# with open("notes.txt","r") as f:
#     data=f.read()
#     print(data)
#     print(len(data))


#2
# with open("notes.txt", "r") as f:
#     data=f.readline().strip()
#     print(data)



#3
# with open("notes.txt", "r")as f:
#     data=[line.strip() for line in f.readlines()]
#     print(data)


#4
# with open("notes.txt", "r")as f:
#     for line in f:
#         data=line.strip()
#         if not data:
#             continue
#         print(data.upper())    



#5
# with open("notes.txt","r")as f:
#     count=0
#     for line in f:
#         data=line.split()
#         count+=len(data)
#     print(f"Total number of words in the file:{count}")   

#6
# with open("dairy.txt","w") as f:
#     f.write("I  learend basics of python\n")
#     f.write("I learned functions \n")
#     f.write("I learned data structures\n")


#7
# with open("dairy.txt","a")as f:
#     f.write("I learned loops concepts")
# with open("dairy.txt","r")as f:
#     data=f.read()
#     print(data)    
    
#8
# with open("square.txt","w")as f:
#     for i in range(1,11):
#         f.write(str(i**2) +"\n")    

# with open ("square.txt","r")as f:
#     data=f.read()
#     print(data)

# total=0
# with open("square.txt","r")as f:
    
#     for line in f:
#         line=line.strip()
#         total+=int(line)
#     print(f'Total sum of the sqares:{total}')

#09
# with open("notes.txt","r")as f:
#     with open("notes_upper.txt", "w")as destination:
#         for line in f:
#             line=line.strip()
#             if not line:
#                 continue
#             destination.write(line.upper()+ "\n")


#10
# import csv
# with open("scores.csv","r")as f:
#     reader=csv.reader(f)
#     header=next(reader)
#     print(header)
#     for row in reader:
#         print(row)

#11
# import csv
# with open("scores.csv","r") as f:
#     reader=csv.DictReader(f)
   
#     for line in reader:
#         print(f"{line['name']}:{line["score"]}")


#12
# import csv
# scores=[]
# with open("scores.csv","r")as f:
#     reader=csv.DictReader(f)
#     for line in reader:
#         if line["score"]!="":
#             scores.append(int(line["score"]))
# print(scores)

# average=sum(scores)/len(scores)
# print(f"Average:{average:.2f}")


#13
# import csv

# students=[
#     ["Surendra",90],
#     ["ram",87],
#     ["prem",67]
# ]

# with open("results.csv","w" , newline="")as f:
#     write=csv.writer(f)
#     write.writerow(["name","score"])
#     write.writerows(students)


#14
#import json
# with open("profile.json","r")as f:
#     data=json.load(f)
# print(data)
# print(data["name"])
# print(len(data["completed_days"]))    
    


#15
# import json
# with open("profile.json","r")as f:
#     data=json.load(f)
# data["completed_days"].append(6)

# with open("profile.json","w")as f:
#     data=json.dump(data,f , indent=2)

#16
# import json
# data={
#     "topic":"function",
#     "durtion_minutes":30,
#     "format":"easy"
# }

# json_string=json.dumps(data,indent=2)
# print(json_string)
# print(type(json_string))

# result=json.loads(json_string)
# print(result)
# print(type(result))


#17
# import json
# import csv
# rows=[]
# with open ("scores.csv","r")as f:
#     reader=csv.DictReader(f)
#     for row in reader:
#         rows.append(dict(row))

# with open("scores.json","w")as f:
#     json.dump(rows,f,indent=2)
    

#18
# try:
#     with open("team.txt","r")as f:
#         data=f.read()
#         print(data)    
# except FileNotFoundError:
#     print("Soryy this does not exist")        


#19
# try:
#     num=int(input("enter the number:"))
#     print(num)
# except ValueError:
#     print("please enter the valid number!")    


#20
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = num1 / num2

#     print("Result:", result)

# except ValueError:
#     print("Please enter valid numbers.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

#21
# try:
#     with open("notesy.txt","r")as f:
#         data=f.read()
#         print(data)
# except FileNotFoundError:
#     print("File not exist")
# else:
#     print("File loaded successfully")
#     print("File length:", len(data))


#22
# try:
#     with open("notes.txt", "r") as f:
#         data = f.read()
#         print(data)

# except FileNotFoundError:
#     print("File does not exist.")

# finally:
#     print("Attempt finished")

#23
# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")

#     return age


# # Valid value
# try:
#     print(check_age(25))
# except ValueError as e:
#     print(e)


# # Invalid value
# try:
#     print(check_age(-5))
# except ValueError as e:
#     print(e)


#24
# class InvalidScoreError(Exception):
#     pass


# def validate_score(score):
#     if score < 0 or score > 100:
#         raise InvalidScoreError("Score must be between 0 and 100")

#     return score


# try:
#     print(validate_score(85))
# except InvalidScoreError as e:
#     print(e)

# try:
#     print(validate_score(150))
# except InvalidScoreError as e:
#     print(e)    



#25
# class InvalidScoreError(Exception):
#     pass


# def validate_score(score):
#     if score < 0 or score > 100:
#         raise InvalidScoreError("Score must be between 0 and 100")

#     return score


# scores = [85, 120, 45, -10, 100]

# for score in scores:
#     try:
#         result = validate_score(score)
#         print(f"{score} is valid")
        
#     except InvalidScoreError as e:
#         print(f"{score} is invalid: {e}")


#26
# import csv

# def load_scores(path):
#     scores = {}

#     try:
#         with open(path, "r") as f:
#             reader = csv.DictReader(f)

#             for row in reader:
#                 try:
#                     score = int(row["score"])
#                     scores[row["name"]] = score

#                 except (ValueError, KeyError):
#                     continue

#     except FileNotFoundError:
#         return {}

#     return scores
# print(load_scores("scores.csv"))

#27
# def summarise(scores):
#     return {
#         "count": len(scores),
#         "average": sum(scores.values()) / len(scores),
#         "highest": max(scores.values()),
#         "lowest": min(scores.values())
#     }


# scores = {
#     "surendra": 89,
#     "ram": 38,
#     "prem": 78,
#     "kiran": 92
# }

# print(summarise(scores))


#28
# def word_frequencies():
#     frequencies = {}

#     with open("notes.txt", "r") as f:
#         for line in f:
#             words = line.lower().split()

#             for word in words:
#                 frequencies[word] = frequencies.get(word, 0) + 1

#     return frequencies

# print(word_frequencies())

#29
# import json

# class MissingConfigKeyError(Exception):
#     pass


# def load_config(path):
#     with open(path, "r") as f:
#         data = json.load(f)

#     if "batch_size" not in data:
#         raise MissingConfigKeyError("Missing 'batch_size' key")

#     if "learning_rate" not in data:
#         raise MissingConfigKeyError("Missing 'learning_rate' key")

#     return data


# try:
#     config = load_config("config.json")
#     print("Config loaded successfully:")
#     print(config)

# except MissingConfigKeyError as e:
#     print(f"Configuration error: {e}")


#30
def parse_log(path):
    logs = []
    skipped = 0

    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(maxsplit=3)

            if len(parts) != 4:
                skipped += 1
                continue

            timestamp = parts[0] + " " + parts[1]
            level = parts[2]
            message = parts[3]

            logs.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })

    print(f"Successfully parsed: {len(logs)}")
    print(f"Skipped: {skipped}")

    return logs


logs = parse_log("access.log")
print(logs)