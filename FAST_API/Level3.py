from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: int

productList = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 20000},
    {"id": 3, "name": "Tablet", "price": 30000}
]


@app.put("/edit_items")
def update_items(item_id: int, item:Item):
    for i in range(len(productList)):
        if productList[i]["id"] == item_id:
            productList[i] = item
            return {
                "message": "Item updated successfully",
                "data": item
            }
    return {"message": "Item not found"} 

@app.delete("/delete_items")
def delete_items(item_id:int):
    for i  in range(len(productList)):
        if productList[i]["id"] == item_id:
            del productList[i]
            return { "messge": "item deleted Successfully"}
    return{"message": "item not found"}
    