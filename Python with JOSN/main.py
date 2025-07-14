# Example 2 - FastAPI with JSON Data

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

# Post Method
@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created!"}

# Get Method
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Sher Bahadur",
        "age": 30,
        "email": "sheru@email.com"
    }