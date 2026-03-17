import pytest
from utils.api_client import APIClient
from data.test_data import valid_login_payload

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticated_client():
    client = APIClient()
    response = client.login(valid_login_payload)
    token = response.json()["token"]
    client.set_token(token)
    return client