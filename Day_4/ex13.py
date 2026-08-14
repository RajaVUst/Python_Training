# Global variable
total_attempts = 0

def log_attempt():
    """Increment the total_attempts counter by 1."""
    global total_attempts
    total_attempts += 1

# Call the function 3 times
log_attempt()
log_attempt()
log_attempt()

# Print the updated value
print(total_attempts)

#Output:
"""PS C:\training\Python_Training> & "C:\Program Files\Python314\python.exe" c:/training/Python_Training/Day_4/ex13.py
3"""