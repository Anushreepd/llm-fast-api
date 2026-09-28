from pydantic import BaseModel


Users = [
    {"id": 1, "name": "Anu", "email": "anu@gmail.com"},
    {"id": 2, "name": "Raj", "email": "raj@gmail.com"}
]
class UserData(BaseModel):
    id: int
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    