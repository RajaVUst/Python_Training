def summarise(scores):
    values = scores.values()

    return {
        "count": len(scores),
        "average": sum(values) / len(scores),
        "highest": max(values),
        "lowest": min(values)
    }

scores = {
    "Amit": 85,
    "Reni": 92,
    "Tara": 78,
    "Sam": 88
}

print(summarise(scores))

# output:
# {'count': 4, 'average': 85.75, 'highest': 92, 'lowest': 78}