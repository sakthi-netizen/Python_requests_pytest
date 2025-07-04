import pytest
import uuid
from utils.api_client import APICLIENT

@pytest.fixture(scope="module")
def api_client():
    return APICLIENT()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_users(api_client,load_user_data):
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data['email'] = unique_email
    
    response = api_client.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == 'John Doe'
    
    id = response.json()['id']
    responseget = api_client.get("users/10")
    assert responseget.status_code == 200
    assert responseget.json()['name'] == 'Clementina DuBuque'

def test_update_users(api_client):
    user_data = {
        "name": "Sakthi",
        "username": "johndoes",
        "email": "johndsakoe@example.com"
    }
    response = api_client.put("users/1", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'Sakthi'

def test_delete_users(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200
