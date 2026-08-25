# Task 6 - Readiness Self-Check
# Written from memory first, then verified against earlier tasks.

# STEP 1 — Written FROM MEMORY (attempt before checking)

# A) Class with constructor and one dunder method 
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name}, ${self.price})"

p = Product("Laptop", 999)
print(p)   # uses __str__


# B) FastAPI endpoint with a Pydantic request model 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class OrderIn(BaseModel):
    product: str
    quantity: int

@app.post("/orders")
def create_order(order: OrderIn):
    return {"product": order.product, "quantity": order.quantity}


# C) Pandas groupby().agg() call 
import pandas as pd

data = {
    "department": ["Eng", "Eng", "HR", "HR", "Mkt"],
    "salary":     [90000, 110000, 55000, 58000, 70000]
}
df = pd.DataFrame(data)

result = df.groupby("department")["salary"].agg(
    avg_salary="mean",
    headcount="count"
).sort_values("avg_salary", ascending=False)

print(result)

# STEP 2 — Verified against earlier tasks (task_4.py / task_2.py / DAY_8)

# Class:     Correct. __init__ takes self first, __str__ returns a string. ✓
# FastAPI:   Correct. Pydantic model as parameter auto-handles @RequestBody + @Valid. ✓
# Pandas:    Correct. groupby + named agg + sort_values. ✓

# STEP 3 — Mistakes found and why

# No mistakes this time. If any had occurred, they would be categorised as:
#   - TYPO:    e.g. wrote __Str__ instead of __str__  (wrong capitalisation)
#   - SYNTAX:  e.g. forgot self in method signature   (missed Python rule)
#   - CONCEPT: e.g. used @RequestBody annotation in FastAPI (Java habit bleeding in)

print("\nReadiness self-check complete — see comments for mistake analysis.")
