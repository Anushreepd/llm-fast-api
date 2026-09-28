from fastapi import FastAPI
from routes import items, users

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to FAST API"

app.include_router(items.router)
app.include_router(users.router)