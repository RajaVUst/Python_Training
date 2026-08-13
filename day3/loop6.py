sentence="Hi i am bonny david"
count=0
vowels="aeiouAEIOU"
for  i in sentence:
    if i in vowels:
        count=count+1

print(count)