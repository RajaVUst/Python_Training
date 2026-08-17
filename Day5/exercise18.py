scores_dict={'Amit': 78, 'Reni': 91, 'Tara': 65}


passed_students = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}

print(passed_students)

'''
{'Amit': 78, 'Reni': 91}

'''


