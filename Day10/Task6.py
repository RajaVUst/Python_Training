class TrainingRun:

    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.learning_rate = learning_rate

    def __str__(self):
        return (
            f"TrainingRun("
            f"model='{self.model_name}', "
            f"lr={self.learning_rate})"
        )


run = TrainingRun("gpt-mini", 0.01)

print(run)


# Output:
# TrainingRun(model='gpt-mini', lr=0.01)



from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class TrainingRequest(BaseModel):

    model_name: str
    learning_rate: float


@app.post("/train")
def train_model(request: TrainingRequest):

    return {
        "model": request.model_name,
        "learning_rate": request.learning_rate
    }


# Example request:
#
# POST /train
#
# {
#     "model_name": "gpt-mini",
#     "learning_rate": 0.01
# }
#
# Output:
# {
#     "model": "gpt-mini",
#     "learning_rate": 0.01
# }



import pandas as pd

employees = pd.DataFrame({
    "name": ["Amit", "Rahul", "Priya", "Neha"],
    "department": ["IT", "IT", "HR", "HR"],
    "salary": [60000, 70000, 50000, 55000]
})

result = (
    employees
    .groupby("department")
    .agg(
        average_salary=("salary", "mean"),
        headcount=("name", "count")
    )
)

print(result)


# Output:
#             average_salary  headcount
# department
# HR                 52500.0           2
# IT                 65000.0           2