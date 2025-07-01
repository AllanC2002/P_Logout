import pytest
from unittest.mock import patch
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["PROPAGATE_EXCEPTIONS"] = True
    with app.test_client() as client:
        yield client

@patch("main.jwt.decode")  # Mock jwt.decode
def test_logout_success(mock_jwt_decode, client):
    # Simulate a successful logout by mocking the jwt.decode function
    mock_jwt_decode.return_value = {"user_id": 123}

    response = client.post(
        "/logout",
        headers={"Authorization": "Bearer valid.jwt.token"}
    )

    assert response.status_code == 200
    assert response.get_json() == {"message": "Logout successful."}
