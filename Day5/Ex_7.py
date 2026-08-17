def stats(numbers):
    temp=[]
    temp.append(max(numbers))
    temp.append(min(numbers))
    temp.append(sum(numbers)//len(numbers))
    return temp
numbers=[1,2,3,4,5,6]
print(stats(numbers))
#ouput
#[6, 1, 3]