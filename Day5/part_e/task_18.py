scores_dict = {
    "Amit": 78,
    "Reni": 91,
    "Tara": 65
}

passed = {
    name: score
    for name, score in scores_dict.items()
    if score >= 70
}

print(passed)


# {'Amit': 78, 'Reni': 91}