# input a string
text = input("Enter a string: ")

# initialize a counter variable to 0
count = 0
# loop through the string
for i in text:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        count = count + 1

# print the count of vowels in the string
print(count)