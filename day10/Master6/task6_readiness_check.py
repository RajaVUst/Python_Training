
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ProductIn(BaseModel):
    name: str
    price: float

@app.post("/products")
def create_product(product: ProductIn):
    return product


import pandas as pd

data = pd.DataFrame({
    "department": ["IT", "IT", "HR"],
    "salary": [60000, 70000, 50000]
})

summary = data.groupby("department").agg(
    average_salary=("salary", "mean"),
    employee_count=("salary", "count")
)

print(Product("Laptop", 50000))
print(summary)

# OUTPUT

# Laptop - 50000
#             average_salary  employee_count
# department                                
# HR                 50000.0               1
# IT                 65000.0               2
