total_attempts=0

    
def log_attempt():
    global total_attempts
    total_attempts=total_attempts+1

log_attempt()
log_attempt()
log_attempt()

print(f"total_attempts={total_attempts}")
    
# OUTPUT
# total_attempts=3
    
    