def summarise(scores):
    values = scores.values()

    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values)
    }

scores = {
    "Aron": 95,
    "Pranav": 88,
    "Chris": 76,
    "Reni": 91
}

print(summarise(scores))

"""
OUTPUT:
{'count': 4, 'average': 87.5, 'highest': 95, 'lowest': 76}
"""