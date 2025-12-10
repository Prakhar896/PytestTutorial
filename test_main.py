import pytest
from main import Database

@pytest.fixture
def db():
    database = Database()
    yield database # Provide fixture instance
    database.data.clear() # Teardown: clear database after each test

def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"

def test_add_existing_user_raises(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Bob")

def test_delete_user(db):
    db.add_user(1, "Alice")
    db.delete_user(1)
    assert db.get_user(1) is None