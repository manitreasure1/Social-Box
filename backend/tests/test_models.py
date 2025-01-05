from .conftest import  TestClient


def test_create_user_model(client: TestClient):
    response = client.post(
        "/users", params={
            "username":"treasview",
            "email": "treasview@example.com", 
            "password": "password123"
            }
    )
    data = response.json()
    assert response.status_code == 200
    assert data['username'] == "treasview"
    
    
