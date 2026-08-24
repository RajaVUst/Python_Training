from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class EmployeeRequest(BaseModel):
    name: str
    department: str
    salary: float


@app.post("/employees")
def create_employee(employee: EmployeeRequest):

    return {
        "message": "Employee created successfully",
        "employee": employee
    }


