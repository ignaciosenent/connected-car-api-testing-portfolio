from data.test_data import valid_login_payload, invalid_login_payload

def test_login_success(api_client):
    response = api_client.login(valid_login_payload)

    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str)
    assert len(data["token"]) > 0

def test_login_invalid_password(api_client):
    response = api_client.login(invalid_login_payload)

    assert response.status_code == 401
    data = response.json()
    assert "error" in data