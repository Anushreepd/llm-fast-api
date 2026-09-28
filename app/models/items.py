from pydantic import BaseModel


Items = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 20000},
    {"id": 3, "name": "Tablet", "price": 30000}
]

class ItemList(BaseModel):
    id: int
    name: str
    price: int

class ItemResponse(BaseModel):
    id: int
    name: str
    price: int