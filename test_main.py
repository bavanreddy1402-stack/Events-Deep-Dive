from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_read_root():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()=={"message":"Hello World!"}

def test_add_numbers():
    response=client.get("/add/1/2")
    assert response.status_code==200
    assert response.json()=={"result":3}

def test_health_check():
    response=client.get("/health")
    assert response.status_code==200
    assert response.json()=={"status":"ok"}