logs = [
    "User logged in",
    "User opened dashboard",
    "User viewed profile",
    "User updated password",
    "User logged out"
]

with open("Day8/log.txt", "w") as file:
    for log in logs:
        file.write(log + "\n")
print("File written successfully")

# # Output: File written successfully


#Read line by line
with open("Day8/log.txt", "r") as file:
    line_number = 1
    for line in file:
        print(line_number, line.strip())
        line_number += 1

# Output:1 User logged in
# 2 User opened dashboard
# 3 User viewed profile
# 4 User updated password
# 5 User logged out


#Manual open and close
file = open("Day8/log.txt", "r")
print(file.read())
file.close()

# Output:
# User logged in
# User opened dashboard
# User viewed profile
# User updated password
# User logged out


file = open("Day8/log.txt", "r")
print(file.read())

#Append instead of overwrite
with open("Day8/log.txt", "a") as file:
    file.write("New user logged in\n")

# Output:
# User logged in
# User opened dashboard
# User viewed profile
# User updated password
# User logged out