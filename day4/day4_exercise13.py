# global variable to store total attempts
total_attempts = 0

def log_attempt():
    global total_attempts
    total_attempts += 1

# call 3 times
log_attempt()
log_attempt()
log_attempt()

print("Total attempts:", total_attempts)

'''
OUTPUT:
Total attempts: 3
'''