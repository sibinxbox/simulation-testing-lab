import os
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from app import create_app

def test_health():
    client = create_app().test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_version():
    client = create_app().test_client()
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json

def test_info():
    client = create_app().test_client()
    response = client.get("/api/info")
    assert response.status_code == 200
    assert response.json["service"] == "simulation-testing-lab"
def test_status():
    client = create_app().test_client()
    response = client.get("/api/status")
    assert response.status_code == 200
    assert response.json["status"] == "running"
