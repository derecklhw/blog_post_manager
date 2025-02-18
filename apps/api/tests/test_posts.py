
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app
from models import Post

client = TestClient(app)

@pytest.fixture
def db_session():
    from database import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_post(db_session: Session):
    response = client.post(
        "/posts/",
        json={"title": "Test Post", "content": "Test Content"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["content"] == "Test Content"

def test_get_all_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_post_by_id(db_session: Session):
    # First create a post
    post = client.post(
        "/posts/",
        json={"title": "Test Post", "content": "Test Content"}
    ).json()
    
    response = client.get(f"/posts/{post['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Post"

def test_update_post(db_session: Session):
    # First create a post
    post = client.post(
        "/posts/",
        json={"title": "Original Title", "content": "Original Content"}
    ).json()
    
    response = client.put(
        f"/posts/{post['id']}",
        json={"title": "Updated Title", "content": "Updated Content"}
    )
    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post["title"] == "Updated Title"
    assert updated_post["content"] == "Updated Content"

def test_delete_post(db_session: Session):
    # First create a post
    post = client.post(
        "/posts/",
        json={"title": "Test Post", "content": "Test Content"}
    ).json()
    
    response = client.delete(f"/posts/{post['id']}")
    assert response.status_code == 204
    
    # Verify post is deleted
    get_response = client.get(f"/posts/{post['id']}")
    assert get_response.status_code == 404

def test_get_nonexistent_post():
    response = client.get("/posts/999999")
    assert response.status_code == 404

def test_create_post_invalid_data():
    response = client.post(
        "/posts/",
        json={"title": "", "content": ""}
    )
    assert response.status_code == 422

def test_update_nonexistent_post():
    response = client.put(
        "/posts/999999",
        json={"title": "Updated Title", "content": "Updated Content"}
    )
    assert response.status_code == 404

def test_delete_nonexistent_post():
    response = client.delete("/posts/999999")
    assert response.status_code == 404
