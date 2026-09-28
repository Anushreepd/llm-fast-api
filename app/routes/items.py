from fastapi import APIRouter, HTTPException, status

from models.items import ItemList, ItemResponse, Items

router = APIRouter()

@router.get("/items", response_model= list[ItemResponse])
def get_items():
    return Items

@router.get("/item/{item_id}", response_model= ItemResponse)
def get_item_id(item_id: int):
    for i in range(len(Items)):
        if Items[i]["id"] == item_id:
            return Items[i]
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail="item not found"
    )

@router.post("/items", response_model= ItemResponse, status_code=status.HTTP_201_CREATED)
def add_items(item: ItemList):
    for existing in Items:
        if existing["id"] != item.id :
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Id mismatch"
            )
    new_data = item.model_dump()
    Items.append(new_data)
    return new_data

@router.put("/item/{item_id}", response_model= ItemResponse)
def update_item(id: int, item: ItemList):
    if id != item.id:
        raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Id already exist"
        )
    for i in range(len(Items)):
        if Items[i]["id"] == id :
            Items[i] = item
            return{"message": "Item updated successfuly"}
    raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="item not found"
        )

@router.delete("/item/{item_id}", response_model= ItemResponse)
def update_item(id: int):
    for i in range(len(Items)):
        if Items[i]["id"] == id :
            del Items[i]
            return{"message": "Item deleted successfuly"}
    raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="item not found"
        )