def  stats(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    average_number = sum(numbers)/len(numbers)

    return (min_number,max_number,average_number)

print(stats([1,2,4,6,8,9]))

"""
Output->
(1, 9, 5.0)
"""