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
    "Priya": 78,
    "Arun": 105
}
result = summarise(scores)
print(result)

# output
# {'count': 4, 'average': 90.0, 'highest': 105, 'lowest': 78}