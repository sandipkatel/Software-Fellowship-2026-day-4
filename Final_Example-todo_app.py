# A Simple ToDo App

from fastapi import FastAPI, Body
import json
import os

app = FastAPI(title="Simple ToDo App",
    description="Sample ToDo application using FastAPI similar to your excercise",
    version="1.0.0")

todo_json = "todos.json"

# if todos.json does not exist, create an empty file
if not os.path.exists(todo_json):
    with open(todo_json, "w") as f:
        json.dump([], f)


@app.get("/todos")
def get_todos():
    """Get all ToDo items."""
    with open(todo_json, "r") as f:
        todos = json.load(f)
    return {
        "message": "List of all ToDo items",
        "todos": todos
    }


@app.post("/todo")
def create_todo(
    todo: dict = Body(
        example={
            "title": "Learn FastAPI",
            "description": "Complete the FastAPI tutorial",
            "completed": False
        }
    )
):
    """Create a new ToDo item."""
    with open(todo_json, "r") as f:
        todos = json.load(f)
    todo_id = len(todos) + 1
    todo["id"] = todo_id
    todos.append(todo)
    with open(todo_json, "w") as f:
        json.dump(todos, f)
    return {
        "message": "ToDo item created successfully",
        "todo": todo
    }


@app.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    """Get a specific ToDo item by ID."""
    with open(todo_json, "r") as f:
        todos = json.load(f)
    for todo in todos:
        if todo['id'] == todo_id:
            return {
                "message": "ToDo item found",
                "todo": todo
            }
    return {
        "message": "ToDo item not found"
    }


@app.put("/todo/{todo_id}")
def update_todo(
    todo_id: int,
    updated_todo: dict = Body(
        example={
            "title": "Updated Todo Title",
            "description": "Updated description",
            "completed": True
        }
    )
):
    """Update a specific ToDo item by ID."""
    # Initialize JSON file if it doesn't exist
    if not os.path.exists(todo_json):
        with open(todo_json, "w") as f:
            json.dump([], f)

    with open(todo_json, "r") as f:
        todos = json.load(f)
    for todo in todos:
        if todo['id'] == todo_id:
            todo.update(updated_todo)
            with open(todo_json, "w") as f:
                json.dump(todos, f)
            return {
                "message": "ToDo item updated successfully",
                "todo": todo
            }
    return {
        "message": "ToDo item not found"
    }


@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    """Delete a specific ToDo item by ID."""
    with open(todo_json, "r") as f:
        todos = json.load(f)
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            with open(todo_json, "w") as f:
                json.dump(todos, f)
            return {
                "message": "ToDo item deleted successfully"
            }
    return {
        "message": "ToDo item not found"
    }
