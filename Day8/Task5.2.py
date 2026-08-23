from abc import ABC, abstractmethod


class Step(ABC):

    @abstractmethod
    def process(self, data):
        pass


class Cleaner(Step):

    def process(self, data):
        return data.strip()


class Tokenizer(Step):

    def process(self, data):
        return data.split()


class Normalizer(Step):

    def process(self, data):
        return [
            word.lower()
            for word in data
        ]


def run_pipeline(steps, data):
    result = data

    for step in steps:
        result = step.process(result)

    return result


steps = [
    Cleaner(),
    Tokenizer(),
    Normalizer()
]

result = run_pipeline(
    steps,
    "  PYTHON Is FUN  "
)

print("ABC pipeline result:", result)


try:
    invalid_step = Step()
except TypeError as error:
    print("Cannot create Step:", error)


# Duck typing is useful for small, flexible systems where objects only need
# to provide the expected method. An ABC is better on larger teams because
# it clearly documents and enforces the required methods.
#
# An ABC is the closer Python equivalent to a Java interface.


#output
'''
ABC pipeline result: ['python', 'is', 'fun']
Cannot create Step: Can't instantiate abstract class Step without an implementation for abstract method 'process'

'''