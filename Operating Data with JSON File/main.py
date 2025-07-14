# Example 4: Reading Data from JSON Files

import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

# Utility functions to load and save users from/to JSON file
def load_users():
    with open('users.json', 'r') as file:
        return json.load(file)


def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=2)


@app.get("/users/")
def get_users():
    """Retrieve all users."""
    users = load_users()
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Retrieve a user by ID."""
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}


@app.post("/users/")
def create_user(user: User):
    """Create a new user."""
    users = load_users()
    new_id = max([u["id"] for u in users]) + 1
    new_user = {"id": new_id, "name": user.name, "age": user.age}
    users.append(new_user)
    save_users(users)
    return new_user