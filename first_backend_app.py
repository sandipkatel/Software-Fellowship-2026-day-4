# Example 1 - Your First FastAPI Application

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Software Fellowship Participant"}


# Use following command to run the FastAPI application:
""" 
pip install fastapi fastapi[standard]
fastapi dev hello.py
"""