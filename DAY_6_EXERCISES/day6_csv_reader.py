import csv

with open("DAY_6_EXERCISES/scores.csv", "r") as f:
    contents = csv.reader(f)

    header = next(contents)
    print(header)

    for line in contents:
        print(line)

"""
Output->
['name', 'score']
['Alice', '95']
['Bob', '110']
['Charlie', '78']
['David', '']
['Eva', '-5']
"""