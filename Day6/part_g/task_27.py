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
    "Alice": 85,
    "Bob": 105,
    "David": 72,
    "Eva": -10
}

summary = summarise(scores)

print(summary)


# {'count': 4, 'average': 63.0, 'highest': 105, 'lowest': -10}