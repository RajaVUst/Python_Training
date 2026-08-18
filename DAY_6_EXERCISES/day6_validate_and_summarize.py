def summarise(scores):
    values = scores.values()

    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values)
    }


scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 76
}

print(summarise(scores))

"""
Output->
{'count': 3, 'average': 86.33333333333333, 'highest': 95, 'lowest': 76}
"""
