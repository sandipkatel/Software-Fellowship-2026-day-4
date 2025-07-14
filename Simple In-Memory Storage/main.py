# Example 3: Simple In-Memory Storage
from fastapi import FastAPI

app = FastAPI()

# Simple "database" (just a list)
users_db = [
    {"id": 1, "name": "KP", "age": 78},
    {"id": 2, "name": "Sheru", "age": 77}
]

@app.get("/users/")
def get_all_users():
    return users_db

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}