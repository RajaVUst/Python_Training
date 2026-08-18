def summarise(scores):
    values = scores.values()

    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values)
    }


scores = {
    "Rahul": 92,
    "Priya": 88,
    "Arjun": 95,
    "Sneha": 90
}

print(summarise(scores))

# Output:
# {'count': 4, 'average': 91.25, 'highest': 95, 'lowest': 88}