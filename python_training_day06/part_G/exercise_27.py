def summarise(scores):
    return {
        "count": len(scores),
        "average": sum(scores.values()) / len(scores),
        "highest": max(scores.values()),
        "lowest": min(scores.values())
    }


scores = {
    "Asha": 85,
    "Rahul": 92,
    "Priya": 105,
    "Meena": 78
}

print(summarise(scores))


#output:
'''{'count': 4, 'average': 90.0, 'highest': 105, 'lowest': 78}'''