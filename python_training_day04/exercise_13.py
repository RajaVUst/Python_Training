total_attempts = 0

def log_attempt():
    global total_attempts
    total_attempts = total_attempts + 1

log_attempt()
log_attempt()
log_attempt()

print("Total attempts:", total_attempts)


#output:
'''Total attempts: 3'''