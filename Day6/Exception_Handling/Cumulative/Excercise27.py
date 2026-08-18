# Validate and summarise

def summarise(scores):

    values = scores.values()
    result = {
        "count": len(scores),
        "average": sum(values) / len(scores),
        "highest": max(values),
        "lowest": min(values)
    }
    return result

scores = {
    "Arun": 80,
    "Bala": 95,
    "Cathy": 70
}
print(summarise(scores))


# Output:
# {'count': 3, 'average': 81.66666666666667, 'highest': 95, 'lowest': 70}