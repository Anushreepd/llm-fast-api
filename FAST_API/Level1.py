from enum import Enum
from fastapi import FastAPI, Query

app = FastAPI()

# -----------------------------
# Sample in-memory employee data
# -----------------------------
employees = [
    {"id": 1, "name": "Anu", "salary": 50000, "department": "IT"},
    {"id": 2, "name": "Ravi", "salary": 70000, "department": "HR"},
    {"id": 3, "name": "John", "salary": 40000, "department": "IT"},
    {"id": 4, "name": "Priya", "salary": 90000, "department": "Finance"},
    {"id": 5, "name": "Kiran", "salary": 30000, "department": "HR"},
]

# -----------------------------
# Basic health / test API
# -----------------------------
@app.get("/message")
def message():
    return {"message": "Welcome to GET API"}

# -----------------------------
# Enum for sorting order
# Ensures only 'asc' or 'desc' is allowed
# -----------------------------
class Order(str, Enum):
    asc = "asc"
    desc = "desc"

# -----------------------------
# GET /employees API
# Supports:
# - Filter by name (partial match)
# - Filter by department
# - Filter by minimum salary
# - Sorting by name (asc/desc)
# -----------------------------
@app.get("/employees")
def get_employees(
    name: str = None,           # Query param: filter by employee name
    department: str = None,     # Query param: filter by department
    min_salary: int = None,     # Query param: filter by minimum salary
    order: Order = Query(Order.asc)  # Sorting order (default: asc)
):
    
    # Start with full employee list
    result = employees

    # -----------------------------
    # Filter by name (case-insensitive)
    # Example: /employees?name=anu
    # -----------------------------
    if name:
        result = [e for e in result if name.lower() in e["name"].lower()]

    # -----------------------------
    # Filter by department
    # Example: /employees?department=IT
    # -----------------------------
    if department:
        result = [e for e in result if department.lower() in e["department"].lower()]

    # -----------------------------
    # Filter by minimum salary
    # Example: /employees?min_salary=50000
    # -----------------------------
    if min_salary:
        result = [e for e in result if e["salary"] >= min_salary]

    # -----------------------------
    # Sort employees by name
    # asc → A-Z
    # desc → Z-A
    # -----------------------------
    result = sorted(
        result,
        key=lambda x: x["name"],
        reverse=(order == Order.desc)
    )

    # Return final filtered + sorted result
    return result