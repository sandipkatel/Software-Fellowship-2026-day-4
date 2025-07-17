from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model
class Todo(BaseModel):
    task: str

# File path for the JSON "database"
DATA_FILE = "todo.json"

# Load todos from file
def load_todos():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save todos to file
def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=4)

# API Endpoints

@app.get("/todos")
def get_todos():
    return load_todos()

@app.post("/todos")
def add_todo(todo: Todo):
    todos = load_todos()
    new_id = max([t["id"] for t in todos], default=0) + 1
    new_todo = {"id": new_id, "task": todo.task}
    todos.append(new_todo)
    save_todos(todos)
    return new_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    todos = load_todos()
    todos = [t for t in todos if t["id"] != todo_id]
    save_todos(todos)
    return {"message": "Deleted"}
