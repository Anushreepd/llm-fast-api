from fastapi import APIRouter, HTTPException, status

from models.users import UserResponse, Users, UserData

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
def getAllUser():
    return Users

@router.get("/users/{user_id}", response_model=UserResponse)
def getUser(user_id: int):
    for user in Users:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail= "User not found"
        )

@router.post("/user", response_model=UserResponse, status_code= status.HTTP_201_CREATED)
def addUser(user_id: int, user_item: UserData):
    for existing in Users:
        if existing["id"] == user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Id already exists"
            )
    new_data = user_item.model_dump()
    Users.append(new_data)
    return new_data

@router.put("/user/{user_id}", response_model=UserResponse)
def EditUser(user_id: int, user_item: UserData):
    for i in range(len(Users)):
        if Users[i]["id"] == user_id:
            Users[i] = user_item
            return {"message": "updated Successfully"}

    raise HTTPException(
                    status_code= status.HTTP_404_NOT_FOUND,
                    detail="item not found"
    )

@router.delete("/User/{User_id}", response_model= UserResponse)
def update_item(id: int):
    for i in range(len(Users)):
        if Users[i]["id"] == id :
            del Users[i]
            return{"message": "Item deleted successfuly"}
    raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="item not found"
        )
