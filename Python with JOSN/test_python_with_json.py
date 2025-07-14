from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    """Test creating a new user"""
    user_data = {
        "name": "John Chamling Rai",
        "age": 27,
        "email": "john@example.com"
    }
    
    response = client.post("/users/", json=user_data)
    
    assert response.status_code == 200
    assert response.json() == {"message": "User John Chamling Rai created!"}

def test_get_user():
    """Test getting a user by ID"""
    user_id = 123
    
    response = client.get(f"/users/{user_id}")
    
    assert response.status_code == 200
    expected_response = {
        "user_id": 123,
        "name": "Sher Bahadur",
        "age": 30,
        "email": "sheru@email.com"
    }
    assert response.json() == expected_response

def test_create_user_invalid_data():
    """Test creating user with invalid data"""
    invalid_user_data = {
        "name": "John Chamling Rai",
        "age": "not_a_number",  # Invalid age
        "email": "john@example.com"
    }
    
    response = client.post("/users/", json=invalid_user_data)
    
    assert response.status_code == 422  # Validation error