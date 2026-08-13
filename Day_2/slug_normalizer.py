title = " My First Python Project!! "

step1 = title.strip()
print("After strip():", step1)

step2 = step1.replace("!!", "")
print("After remove !!:", step2)

step3 = step2.lower()
print("After lower():", step3)

slug = step3.replace(" ", "_")
print("Final slug:", slug)