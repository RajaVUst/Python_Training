from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


class TrainingRun:
	def __init__(self, model_name, learning_rate):
		self.model_name = model_name
		self.learning_rate = learning_rate

	def __str__(self):
		return (
			f"TrainingRun(model='{self.model_name}', "
			f"learning_rate={self.learning_rate})"
		)


class PredictionRequest(BaseModel):
	text: str
	max_tokens: int = 100


app = FastAPI()


@app.post("/predict")
def predict(request: PredictionRequest):
	return {
		"text": request.text,
		"max_tokens": request.max_tokens,
	}


employees = pd.read_csv(
	Path(__file__).resolve().parents[1] / "employees.csv"
)

department_summary = (
	employees.groupby("department")
	.agg(
		average_salary=("salary", "mean"),
		employee_count=("name", "count"),
	)
	.reset_index()
)


def run_self_check():
	training_run = TrainingRun("gpt-mini", 0.01)
	assert str(training_run) == (
		"TrainingRun(model='gpt-mini', learning_rate=0.01)"
	)

	request = PredictionRequest(text="hello", max_tokens=20)
	assert predict(request) == {"text": "hello", "max_tokens": 20}

	assert set(department_summary.columns) == {
		"department",
		"average_salary",
		"employee_count",
	}
	assert department_summary["employee_count"].sum() == len(employees)

	mistake_log = []
	print("All three snippets passed the readiness self-check.")
	print("Mistake log:", mistake_log or "No mistakes identified.")


if __name__ == "__main__":
	run_self_check()
