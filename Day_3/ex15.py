# 15: Vowel counter
text=input("Enter text: ")
vowels="aeiou"
text=text.lower()
count=0
#by accessing the index
for i in range(len(text)):
    if text[i] in vowels:
          count+=1
print("Vowel count is: ",count)

#by acessing letter only
for i in text:
    if i in vowels:
          count+=1
print("Vowel count is: ",count)