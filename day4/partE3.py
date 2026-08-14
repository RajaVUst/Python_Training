
string="Python Bootcamp"

def count_vowels(string):
    count=0
    vowels="aeiouAEIOU"
    for i in string:
        if i in vowels:
            count=count+1
    
    print(f"count of vowels in string:{count}")

count_vowels(string)
            
# OUTPUT

# count of vowels in string:4
    