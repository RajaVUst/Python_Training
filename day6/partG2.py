def summarise(scores):
    values = list(scores.values())
    summary = {}

    if len(values) == 0:
        summary["count"] = 0
        summary["average"] = 0
        summary["highest"] = None
        summary["lowest"] = None
    else:
        summary["count"] = len(values)
        summary["average"] = sum(values) / len(values)
        summary["highest"] = max(values)
        summary["lowest"] = min(values)

    return summary


valid_scores = {"Asha": 92, "Ben": 85, "Chen": 78, "Divya": 95}
print(summarise(valid_scores))

# OUTPUT

# {'count': 4, 'average': 87.5, 'highest': 95, 'lowest': 78}
