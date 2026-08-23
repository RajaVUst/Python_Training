class DuckCleaner:

    def process(self, data):
        return data.strip()


class DuckTokenizer:

    def process(self, data):
        return data.split()


class DuckNormalizer:

    def process(self, data):
        return [
            word.lower()
            for word in data
        ]


def run_duck_pipeline(steps, data):
    result = data

    for step in steps:
        result = step.process(result)

    return result


duck_steps = [
    DuckCleaner(),
    DuckTokenizer(),
    DuckNormalizer()
]

duck_result = run_duck_pipeline(
    duck_steps,
    "  PYTHON Is FUN  "
)

print("Duck-typed result:", duck_result)


#output

'''
Duck-typed result: ['python', 'is', 'fun']
'''