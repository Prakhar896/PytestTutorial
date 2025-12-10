import pytest
from main import app, users

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client # Provide test client instance

@pytest.fixture(autouse=True)
def clear_users():
    users.clear()  # Clear the users dictionary before each test

def test_add_user(client):
    response = client.post('/users', json={"id": 1, "name": "Alice"})
    
    assert response.status_code == 201
    assert response.json == {"id": 1, "name": "Alice"}
    assert users.get(1) == "Alice"

def test_get_user(client):
    client.post('/users', json={"id": 2, "name": "Bob"})
    
    response = client.get('/users/2')
    
    assert response.status_code == 200
    assert response.json == {"id": 2, "name": "Bob"}
    assert users.get(2) == "Bob"