#De-duplicating Attendance

attendance = ["amit", "reni", "amit", "tara", "reni", "sam","Logesh"]

unique_attendees = set(attendance)
print(unique_attendees)
print("Number of unique people:", len(unique_attendees))


# Output:
# {'amit', 'sam', 'Logesh', 'reni', 'tara'}
# Number of unique people: 5