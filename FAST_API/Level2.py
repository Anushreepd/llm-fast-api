from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    id: int
    name: str
    price: int

items = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 20000},
    {"id": 3, "name": "Tablet", "price": 30000}
]

@app.get("/items")
def ListItems():
    return items

@app.post("/addItems")
def AddNewItems(item: Item):
    for existing in items:
        if existing["id"] == item .id:
            return { "message": "ID already exist"}
    items.append(item.dict())
    return {
        "message": "item added successfully",
        "data": item
    }