email=input("enter the email:")
answer=email.split("@")
username=answer[0]
domain=answer[1]
print(f"The username from the Email is :{username}")
print(f"The email from the email is:{domain}")