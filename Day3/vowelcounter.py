word=input("enter the sentance or word:")
count=0
for i in range(0,len(word)):
    if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u" or word[i]=="A" or word[i]=="E" or word[i]=="I" or word[i]=="O" or word[i]=="U":
        count+=1
print(f"Total number of vowel in sentance is:{count}")